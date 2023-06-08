
import requests

g_server    = "http://127.0.0.1:9000/"
g_user_name = "Administrator"
g_password  = "asdasd"

g_query_server = 'http://localhost:8093/'
g_index_server = 'http://localhost:9108/'

def GetServer():
    return g_server

def GetUserName():
    return g_user_name

def GetPassword():
    return g_password

def GetAuth():
    return (g_user_name, g_password)

def GetQueryServer():
    return g_query_server

def GetIndexServer():
    return g_index_server

def Setup():
    global g_query_server, g_index_server
    query_urls, index_urls = get_query_and_index_urls()
    if query_urls != None:
        g_query_server = "http://{0}/".format(query_urls[0])
    if index_urls != None:
        g_index_server = "http://{0}/".format(index_urls[0])

def get_query_and_index_urls():
    # Replace with your cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Set the Couchbase REST API endpoint URL
    server = GetServer()
    url = server + 'pools/default/nodeServices'

    # Set the request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the GET request to retrieve the node services information
    response = requests.get(url, headers=headers, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        # Process the node services information
        node_services_info = response.json()
        query_urls = []
        index_urls = []

        for node in node_services_info['nodesExt']:
            hostname = node.get('hostname', '127.0.0.1')
            if 'n1ql' in node['services']:
                query_urls.append(hostname + ':' + str(node['services']['n1ql']))
            if 'indexHttp' in node['services']:
                index_urls.append(hostname + ':' + str(node['services']['indexHttp']))

        print("Query URLs: ", query_urls)
        print("Index URLS: ", index_urls)
        return query_urls, index_urls
    else:
        print('Error retrieving node services information:', response.status_code)
        return None, None

