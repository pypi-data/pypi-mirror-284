# Copyright IBM Corp. 2024

# type: ignore
from graphql import GraphQLField
from .constants import bcolors


# Takes a string of comma-separated values as input and adds a dollar sign ($)
# after each value, returning the updated string.
def add_dollar_after_comma(input_string: str) -> str:
    words = input_string.split(", ")
    updated_words = [f"${word}" if word.strip() else word for word in words]
    return ", ".join(updated_words)


# Take a string that contains a list of variables and their types,
# and convert it into a string that contains only the variable names, prefixed with a $.
def convert_to_variable_names(input_string: str) -> str:
    words = input_string.split(", ")
    updated_words = []
    for word in words:
        parts = word.split(": ")
        variable_name = parts[0]
        updated_words.append(f"{variable_name}: ${variable_name}")
    return ", ".join(updated_words)


# Takes an object as input and returns a string representation of the object by
# concatenating the key-value pairs of the object into a comma-separated list.
# The keys and values are separated by a colon and a space.
def object_to_string(obj: dict) -> str:
    string_parts = []
    for key, value in obj.items():
        string_parts.append(f"{key}: {value}")
    return ", ".join(string_parts)


# Takes two dictionaries as input and compares their keys.
# It then removes any keys from the second dictionary that are not present in the first dictionary.
# Finally, it returns a string representation of the resulting dictionary.
def compare_and_remove_fields(object_one: dict, object_two: dict) -> str:
    # Get the keys present in object_one
    keys_one = set(object_one.keys())

    # Remove keys from object_two that are not in object_one
    object_two = {key: value for key, value in object_two.items() if key in keys_one}

    return object_to_string(object_two)


# Takes in an array of items and returns a string representation of those items.
# The function iterates over each item in the array and checks its type.
def create_string_from_array(arr):
    names = []
    for item, value in arr.items():
        if isinstance(value, GraphQLField):
            names.append(item)
        elif isinstance(value, dict):
            item = f"{item} {{{  format_fields(value) }}}"
            names.append(item)

    return " ".join(names)


# Takes two dictionaries as input and returns a new dictionary containing
# only the key-value pairs that are present in the first dictionary.
# The new dictionary will contain all the key-value pairs from the first dictionary,
# but only those keys that are also present in the second dictionary.
def generate_variables(object_one: dict, object_two: dict) -> dict:
    # Get the keys present in object_one
    keys_one = set(object_two.keys())
    return {key: value for key, value in object_one.items() if key in keys_one}


# Takes two dictionaries as input and returns a new dictionary that contains
# all the key-value pairs from the first dictionary except those that are also
# present in the second dictionary. The function uses a set comprehension to
# get the keys from the second dictionary and then filters out any keys that
# are present in the first dictionary using the not keyword.
def remove_variables(object_one: dict, object_two: dict) -> dict:
    # Get the keys present in object_one
    keys_one = set(object_two.keys())
    return {key: value for key, value in object_one.items() if not key in keys_one}


# Takes a dictionary of fields and their values as input and returns
# a string representation of the fields in the GraphQL query format.
# The function handles nested dictionaries by recursively calling itself on the nested dictionaries.
def format_fields(fields: dict) -> str:
    formatted_fields = ""
    for field in fields:
        field_value = fields[field]
        if isinstance(field_value, dict):
            formatted_fields += f"{field} {{ {format_fields(field_value)}}} "
        else:
            formatted_fields += f"{field} "

    return formatted_fields


# Build the arguments string for a GraphQL query.
# If variables are provided that are not in the schema, non_existing_args,
# the variables are removed and a notice is provided.
def args_string_builder(vars, arguments, name):
    if arguments and vars:
        # Check if the variables exist in the provided operation. If it does not, remove the variable and notify the user
        non_existing_args = remove_variables(vars, arguments)
        if non_existing_args:
            print(
                f"{bcolors.WARNING}Notice:{bcolors.ENDC} removed variables {bcolors.CYAN}{bcolors.BOLD}{non_existing_args}{bcolors.ENDC} as those are not found for operation {bcolors.CYAN}{bcolors.BOLD}{name}{bcolors.ENDC}"
            )
        formatted_query = compare_and_remove_fields(vars, arguments)
        args_string = convert_to_variable_names(formatted_query)
        top_level_args_string = add_dollar_after_comma(formatted_query)

        # Generate the custom query
        top_level_args_string = (
            f"({top_level_args_string})" if top_level_args_string else ""
        )
        args_string = f"({args_string})" if args_string else ""

        if top_level_args_string and args_string:
            return top_level_args_string, args_string

    return "", ""
