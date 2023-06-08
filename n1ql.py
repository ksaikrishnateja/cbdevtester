
import requests

from .config import GetUserName, GetPassword, GetQueryServer

def ExecN1QL(query):
    # Replace with your cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Set the request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Set the request payload
    payload = {
        'statement': query
    }

    url = "{0}query/service".format(GetQueryServer())

    # Send the POST request to execute the N1QL query
    response = requests.post(url, headers=headers, auth=(username, password), json=payload)

    # Check the response status code
    if response.status_code == 200:
        # Process the query result
        result = response.json()
        return result, None
    else:
        #print('Error executing N1QL query:', response.text)
        return Node, response.text
