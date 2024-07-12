# Copyright IBM Corp. 2024

# type: ignore
import requests

# type: ignore
from graphql import (
    build_schema,
    build_client_schema,
    get_introspection_query,
    GraphQLField,
    GraphQLInputField,
    GraphQLObjectType,
    GraphQLList,
    GraphQLSchema,
    GraphQLWrappingType,
    GraphQLNamedType,
    GraphQLUnionType,
    print_schema,
)
from typing import Union, Optional

Field = Union[GraphQLField, GraphQLInputField]


# Takes a GraphQLField object as an argument and returns the
# underlying GraphQLNamedType object that the field returns.
def unwrap_field_type(field: Field) -> GraphQLNamedType:
    """Get the underlying field type which is not wrapped."""
    type_ = field.type
    while isinstance(type_, GraphQLWrappingType):
        type_ = type_.of_type
    return type_


# Takes a dictionary of field names and their corresponding field types as input and
# returns a new dictionary containing only those fields whose corresponding field types
# are not graphql parent types.
# If at max_depth, return only the items that do not have children for query.
def remove_graphql_parent_types(fields: dict):
    return {
        k: v
        for k, v in fields.items()
        if not isinstance(
            unwrap_field_type(v), (GraphQLObjectType, GraphQLList, GraphQLUnionType)
        )
    }


# Checks if a given field is a valid GraphQL parent type.
def is_graphql_parent_type(unwrapped_field: str):
    return isinstance(
        unwrapped_field, (GraphQLObjectType, GraphQLList, GraphQLUnionType)
    )


# Handles GraphQL union types by returning a list of their member types.
# If the input field is not a union type, it returns None.
def handle_union_types(unwrapped_field):
    return (
        unwrapped_field.types
        if (isinstance(unwrapped_field, (GraphQLUnionType)))
        else None
    )


# Takes a dictionary of GraphQL fields and recursively builds nested fields up to a maximum depth.
# It handles union types by building nested fields for each type in the union or interface.
def build_nested_fields(
    sub_fields: dict, depth: Optional[int] = 0, max_depth: Optional[int] = 5
):
    for x in sub_fields:
        unwrapped_field = unwrap_field_type(sub_fields[x])
        if is_graphql_parent_type(unwrapped_field):
            union_types = handle_union_types(unwrapped_field)
            if depth < (max_depth - 1):
                unionFields = {}
                if union_types:
                    for y in union_types:
                        unionFields[str(f"... on {y}")] = y.fields
                        build_nested_fields(y.fields, depth + 1, max_depth)
                        sub_fields[x] = unionFields
                else:
                    sub_fields[x] = unwrapped_field.fields
                    build_nested_fields(sub_fields[x], depth + 1, max_depth)
            else:
                if union_types:
                    for y in union_types:
                        sub_fields[x] = remove_graphql_parent_types(y.fields)
                else:
                    sub_fields[x] = remove_graphql_parent_types(unwrapped_field.fields)

    return sub_fields


# Takes a dictionary of GraphQL fields and a maximum depth as input, and
# returns a new dictionary that includes all the original fields plus any
# nested fields that are not parent types. The maximum depth parameter
# determines how many levels of nesting should be included in the output.
def build_fields(field_dict: dict, max_depth: int):
    fields = {}
    for field_name in field_dict:
        unwrapped_field = unwrap_field_type(field_dict[field_name])
        if is_graphql_parent_type(unwrapped_field):
            if max_depth > 1:
                union_types = handle_union_types(unwrapped_field)
                if union_types:
                    for y in union_types:
                        fields.update(
                            {
                                field_name: {
                                    str(f"... on {y}"): build_nested_fields(
                                        y.fields, 1, max_depth
                                    )
                                }
                            }
                        )
                else:
                    fields.update(
                        {
                            field_name: build_nested_fields(
                                unwrapped_field.fields, 1, max_depth
                            )
                        }
                    )
            elif max_depth == 1:
                fields.update(
                    {field_name: remove_graphql_parent_types(unwrapped_field.fields)}
                )
        else:
            fields.update({field_name: field_dict[field_name]})

    return fields


# Takes an operation type (e.g., Query or Mutation) and a query name
# as input and returns the corresponding query type and arguments.
def find_operation(operationType: str, queryName: str):
    queryType = [
        unwrap_field_type(operationType.fields[name])
        for name in operationType.fields
        if name == queryName
    ][0]
    arguments = [
        operationType.fields[name] for name in operationType.fields if name == queryName
    ][0].args
    for name, argument in arguments.items():
        arguments.update({name: argument.type})

    return queryType, arguments


# Takes a GraphQL schema and a query name as input, and
# returns a tuple containing the query's arguments, fields,
# and operation type.
def get_query_properties(
    schema: Union[str, GraphQLSchema],
    queryName: str = None,
    max_depth: Optional[int] = 5,
):
    parsed_schema = build_schema(schema)
    query = parsed_schema.query_type
    mutation = parsed_schema.mutation_type
    if mutation is None and query is None:
        raise Exception("No mutations or queries found in this schema")

    arguments = {}
    queryType = ""
    operationType = ""
    if query is not None and queryName in query.fields:
        operationType = query
        (queryType, arguments) = find_operation(query, queryName)
    elif mutation is not None and queryName in mutation.fields:
        operationType = mutation
        (queryType, arguments) = find_operation(mutation, queryName)
    else:
        raise Exception("No mutations or queries found in this schema")

    return (
        arguments,
        build_fields(queryType.fields, max_depth),
        operationType.name.lower(),
    )


def introspection_result_to_sdl(data: dict[str, any]) -> str:
    client_schema = build_client_schema(data)
    return print_schema(client_schema).strip()


def load_schema(url: str, headers: dict) -> str:
    resp = requests.post(
        url, json={"query": get_introspection_query()}, headers=headers
    )
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise SystemExit(str(e))

    # Must have been a 200 status code
    data = resp.json()
    return introspection_result_to_sdl(data["data"])
