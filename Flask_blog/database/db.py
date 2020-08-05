import pymongo
from flask_pymongo import PyMongo


class Mongo(PyMongo):
    def __init__(self, app, database="test", collection="user"):
        """
        Class to work with mongoDB
        :arg database - database you will use
        :arg collection - collection you wii use
        """
        super().__init__(app=app)
        mongo_client = pymongo.MongoClient('localhost', 2717)
        db = mongo_client[database]
        self.collection = db[collection]

    def find(self, how_many="one", data_filter=None, projection={}):
        """:arg how_many how many results should be returned
        :arg data_filter filter data to return
        :arg projection specify whose columns values should be returned
        :return string or list"""
        if data_filter is None:
            data_filter = {}
        if how_many == "one":
            return self.collection.find_one(data_filter, projection)
        elif how_many == "all":
            cursor = self.collection.find(data_filter,projection)
            return [document for document in cursor]
