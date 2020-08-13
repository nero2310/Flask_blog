from typing import Dict

from pymongo import MongoClient


class Mongo:
    def __init__(self, database="test", collection="user"):
        """
        Class to work with mongoDB
        :arg database - database you will use
        :arg collection - collection you wii use
        """
        mongo_client = MongoClient("mongodb://172.16.0.2:2717/?readPreference=primary&appname=MongoDB%20Compass"
                                   "%20Beta&ssl=false")
        db = mongo_client[database]
        self.collection = db[collection]

    def find(self, how_many="one", data_filter=None, projection=None):
        """:arg how_many how many results should be returned possible values "one" or "all"
        :arg data_filter filter data to return
        :arg projection specify whose columns values should be returned
        :return Dict or None if nothing found"""
        if projection is None:
            projection = {}

        if data_filter is None:
            data_filter = {}

        if how_many == "one":
            return self.collection.find_one(data_filter, projection)

        elif how_many == "all":
            cursor = self.collection.find(data_filter, projection)
            return [document for document in cursor]

    def insert(self, data_to_insert: Dict):
        """:arg data_to_insert data whose wil be inserted into database"""
        self.collection.insert_one(data_to_insert)

    def aggregate(self):
        self.collection.aggregate()
