
from .config import GetServer, GetUserName, GetPassword

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

def load_data(bucket_name, collection_name, data):
    server_url = GetServer()
    username = GetUserName()
    password = GetPassword()

    cluster = Cluster(server_url)
    authenticator = PasswordAuthenticator(username, password)
    cluster.authenticate(authenticator)
    bucket = cluster.bucket(bucket_name)
    collection = bucket.collection(collection_name)

    insert_results = collection.insert_multi(data)

    for key in data:
        print("Inserted Document:", key)
        print("CAS:", insert_results[key].cas)

# Example usage
documents = {
    "user_111": {"id": "user_111", "email": "tom_the_cat@gmail.com"},
    "user_222": {"id": "user_222", "email": "jerry_mouse@gmail.com"},
    "user_333": {"id": "user_333", "email": "mickey_mouse@gmail.com"}
}

load_data('bucket_name', 'collection_name', documents)
