from .deps.auths import Auths
from .db.collection import Collection
import httpx
class PocketBase:
    def __init__(self, host_url, username, password):
        self.host_url = host_url
        self.username = username
        self.password = password

        self.auths = Auths(self.username, self.password, self.host_url)
        self.session = httpx.Client()

    def get_collection(self, collection_name, token=None):
        return Collection(self, collection_name, token)
    
    def create_record(self, collection_name, record, token=None):
        collection = self.get_collection(collection_name, token)
        return collection.create_record(record, token)
    
    def get_record_by_id(self, collection_name, record_id, token=None):
        collection = self.get_collection(collection_name, token)
        return collection.get_record_by_id(record_id, token)
    
    def update_record(self, collection_name, record_id, record, token=None):
        collection = self.get_collection(collection_name, token)
        return collection.update_record(record_id, record, token)
    
    def delete_record(self, collection_name, record_id, token=None):
        collection = self.get_collection(collection_name, token)
        return collection.delete_record(record_id, token)
    
    def create_collection(self, collection, db_type, schema):
        return self.get_collection(collection).create_collection(collection, db_type, schema)
    
    def get_token(self):
        return self.auths.get_token()