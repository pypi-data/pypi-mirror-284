# Copyright IBM Corp. 2024
import requests
import json


# executes a custom GraphQL query name to a GraphQL endpoint.
def execute(endpoint, apikey, name, question):
    # Generate the custom query
    # Optional improvement is to introspect the endpoint to
    # ensure this query structure exists in the schema.
    query = f"query {name}($input: String!) {{{name}(input: $input)}}"

    # Provide an apikey to the endpoint
    # If an apikey is passed, it is compliant with the stepzen apikey structure.
    headers = {}
    if apikey:
        headers = {"Authorization": f"apikey {apikey}"}
    else:
        headers = {}

    # the question being passed into the query
    variables = {"input": question}

    try:
        r = requests.post(
            endpoint, json={"query": query, "variables": variables}, headers=headers
        )

        data = r.json()

        return data
    except KeyError as e:
        return e
