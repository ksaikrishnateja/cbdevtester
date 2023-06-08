#!/usr/bin/env python3

import time
import requests

from .config import GetServer, GetUserName, GetPassword, GetAuth

g_headers = {"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"}

def AddBucket(bucket_name, bucket_type='couchbase', ram_quota_mb=100, replica_count=0):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Set the request data
    data = {
        'name': bucket_name,
        'bucketType': bucket_type,
        'ramQuotaMB': ram_quota_mb,
        'replicaNumber': replica_count
    }

    # Send the POST request to add the bucket
    response = requests.post(url, headers=headers, auth=(username, password), data=data)

    # Check the response status code
    if response.status_code == 202:
        print(f'Successfully added bucket: {bucket_name}')
    else:
        print('Error adding bucket:', response.text)

def AddScope(bucket_name, scope_name):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}/scopes'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Set the request data
    data = {
        'name': scope_name
    }

    # Send the POST request to add the scope
    response = requests.post(url, headers=headers, auth=(username, password), data=data)

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully added scope: {scope_name}')
    else:
        print('Error adding scope:', response.text)

def AddCollection(bucket_name, scope_name, collection_name):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}/scopes/{scope_name}/collections'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Set the request data
    data = {
        'name': collection_name
    }

    # Send the POST request to add the collection
    response = requests.post(url, headers=headers, auth=(username, password), data=data)

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully added collection: {collection_name}')
    else:
        print('Error adding collection:', response.text)

def DeleteBucket(bucket_name):
    # Replace with your cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Set the Couchbase REST API endpoint URL
    url = "{0}/pools/default/buckets/{1}".format(GetServer(), bucket_name)

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the DELETE request to delete the bucket
    response = requests.delete(url, headers=headers, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully deleted bucket: {bucket_name}')
    else:
        print('Error deleting bucket:', response.text)

def DeleteScope(bucket_name, scope_name):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}/scopes/{scope_name}'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the DELETE request to delete the scope
    response = requests.delete(url, headers=headers, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully deleted scope: {scope_name}')
    else:
        print('Error deleting scope:', response.text)

def DeleteCollection(bucket_name, scope_name, collection_name):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}/scopes/{scope_name}/collections/{collection_name}'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the DELETE request to delete the collection
    response = requests.delete(url, headers=headers, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully deleted collection: {collection_name}')
    else:
        print('Error deleting collection:', response.text)

def SetFlushEnabled(bucket_name, flush_enabled):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    current_settings = dict()

    # Update the flush enablement status
    current_settings['flushEnabled'] = flush_enabled

    # Send the POST request to update the bucket
    response = requests.post(url, headers=headers, auth=(username, password), data=current_settings)

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully modified flush enablement for bucket: {bucket_name}')
    else:
        print('Error modifying flush enablement:', response.text)

def FlushBucket(bucket_name):
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/pools/default/buckets/{bucket_name}/controller/doFlush'

    # Send the POST request to flush the bucket
    response = requests.post(url, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        print(f'Successfully flushed bucket: {bucket_name}')
    else:
        print('Error flushing bucket:', response.text)

def LoadTravelSample():
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/sampleBuckets/install'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the POST request to load the "travel-sample" bucket
    response = requests.post(url, headers=headers, auth=(username, password), data='["travel-sample"]')

    # Check the response status code
    if response.status_code == 202:
        print('Successfully initiated the load of the "travel-sample" bucket')
    else:
        print('Error loading the "travel-sample" bucket:', response.text)

def LoadBeerSample():
    # Get the cluster credentials
    username = GetUserName()
    password = GetPassword()

    # Get the server URL
    server_url = GetServer()

    # Set the Couchbase REST API endpoint URL
    url = f'{server_url}/sampleBuckets/install'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the POST request to load the "beer-sample" bucket
    response = requests.post(url, headers=headers, auth=(username, password))

    # Check the response status code
    if response.status_code == 202:
        print('Successfully initiated the load of the "beer-sample" bucket')
    else:
        print('Error loading the "beer-sample" bucket:', response.text)

if __name__=="__main__":
    #g_new_scope = "my_scope"
    #g_colln_prefix = "my_colln_"
    #status = AddScope(g_new_scope)
    #if status:
    #    for i in range(1000):
    #        g_colln_name = "{0}_{1}{2}".format(g_new_scope, g_colln_prefix, i)
    #        AddCollection(g_colln_name, g_scope_name)
    #        time.sleep(0.5)
    AddBucket("bucket-1", 500)
    AddBucket("bucket-2", 100)
    AddBucket("bucket-3", 100)
    AddBucket("bucket-4", 100)
    AddBucket("bucket-5", 100)
    #for i in range(9):
    #    time.sleep(3)
    #    AddBucket("bucket{0}".format(i), 200)

