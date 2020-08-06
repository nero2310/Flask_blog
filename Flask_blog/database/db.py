from pymongo import MongoClient
from typing import Dict
from flask_pymongo import PyMongo


class Mongo:
    def __init__(self,database="test", collection="user"):
        """
        Class to work with mongoDB
        :arg database - database you will use
        :arg collection - collection you wii use
        """
        mongo_client = MongoClient('localhost', 2717)
        db = mongo_client[database]
        self.collection = db[collection]

    def find(self, how_many="one", data_filter=None, projection={}):
        """:arg how_many how many results should be returned possible values "one" or "all"
        :arg data_filter filter data to return
        :arg projection specify whose columns values should be returned
        :return string or list"""
        if data_filter is None:
            data_filter = {}
        if how_many == "one":
            return self.collection.find_one(data_filter, projection)
        elif how_many == "all":
            cursor = self.collection.find(data_filter, projection)
            return [document for document in cursor]

    def insert(self,data_to_insert:Dict):
        """:arg data_to_insert data whose wil be inserted into database"""
        self.collection.insert_one(data_to_insert)