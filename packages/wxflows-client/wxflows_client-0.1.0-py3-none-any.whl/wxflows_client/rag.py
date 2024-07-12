# Copyright IBM Corp. 2024
import requests  # type: ignore
from graphql import (  # type: ignore
    GraphQLField,
    GraphQLInputField,
    GraphQLObjectType,
    GraphQLInterfaceType,
    get_introspection_query,
    ArgumentNode,
    SelectionNode,
)
from .utils.build_query import (
    args_string_builder,
    generate_variables,
    create_string_from_array,
)
from .utils.graphql_helpers import get_query_properties, load_schema
from .utils.utils import error_parameter_types
from typing import List, Union, Optional, Tuple

InterfaceOrObject = Union[GraphQLObjectType, GraphQLInterfaceType]
Field = Union[GraphQLField, GraphQLInputField]
SelectionNodes = List[SelectionNode]
FieldNodeInput = Tuple[List[ArgumentNode], Optional[SelectionNodes]]


# executes a custom GraphQL query name to a GraphQL endpoint.
def execute(
    endpoint: str,
    apikey: str,
    name: str,
    vars: Optional[dict] = None,
    query: Optional[str] = None,
    max_depth: Optional[int] = 5,
):
    error_parameter_types(endpoint, apikey, name, vars, query, max_depth)
    # Provide an apikey to the endpoint
    # If an apikey is passed, it is compliant with the stepzen apikey structure.
    headers = {}
    if apikey:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"apikey {apikey}",
        }
    else:
        headers = {}

    # Get the introspection query
    introspection_query = get_introspection_query(descriptions=True)

    # Send the introspection query to the GraphQL endpoint
    response = requests.post(
        endpoint, json={"query": introspection_query}, headers=headers
    )

    # Parse the response as a GraphQL document
    introspection_result = response.json()

    if "errors" in introspection_result:
        print(introspection_result["errors"])

    schema = load_schema(endpoint, headers)
    arguments, fields, operationType = get_query_properties(schema, name, max_depth)
    fields = create_string_from_array(fields)

    defaultVariables = {
        "n": 10,
        "question": "who are the interns in greys anatomy season 9?",
        "aiEngine": "BAM",
        "model": "ibm/granite-13b-chat-v2",
        "collection": "longnq",
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.7,
        },
    }

    # Filter the object based on the string
    top_level_args_string, args_string = args_string_builder(vars, arguments, name)
    operation = (
        f"{operationType} {name}{top_level_args_string}{{{name}{args_string}{{{fields}}}}}"
        if not query
        else query
    )

    # Provide an apikey to the endpoint
    # If an apikey is passed, it is compliant with the stepzen apikey structure.
    headers = {}
    if apikey:
        headers = {"Authorization": f"apikey {apikey}"}
    else:
        headers = {}

    # Overwritting all variables to defaultVariables
    vars = vars if isinstance(vars, dict) else {}
    variables = {**defaultVariables, **vars}
    # If the variables provided do not exist in the schema for the specified query,
    # remove the variables and execute the query.
    variables = generate_variables(variables, arguments)

    try:
        r = requests.post(
            endpoint, json={"query": operation, "variables": variables}, headers=headers
        )

        data = r.json()

        return data
    except KeyError as e:
        return e
