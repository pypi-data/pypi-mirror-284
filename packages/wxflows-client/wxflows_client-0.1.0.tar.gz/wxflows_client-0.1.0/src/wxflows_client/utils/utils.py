# Copyright IBM Corp. 2024

from typing import Optional


# Raise Errors if the proper types are not provided to the rag.execute() function
def error_parameter_types(
    endpoint: str,
    apikey: str,
    name: str,
    vars: Optional[dict],
    query: Optional[str],
    max_depth: Optional[int],
):
    # Check if vars is a dictionary
    if not isinstance(endpoint, str):
        raise TypeError("endpoint must be a string type")

    # Check if vars is a dictionary
    if not isinstance(apikey, str):
        raise TypeError("apikey must be a string type")

    # Check if vars is a dictionary
    if not isinstance(name, str):
        raise TypeError("name must be a string type")

    if not isinstance(query, Optional[str]):
        raise TypeError("query must be a string type")

    # Check if vars is a dictionary
    if not isinstance(vars, Optional[dict]):
        raise TypeError("vars must be a dictionary type")

    # Check if max_depth is an integer
    if not isinstance(max_depth, Optional[int]):
        raise TypeError("max_depth must be an integer")

    # ISINSTANCE AND CONDITIONAL SECTION

    # Check if max_depth is greater than or equal to 0
    if isinstance(max_depth, int) and max_depth < 0:
        raise ValueError("max_depth must be greater than or equal to 0")
