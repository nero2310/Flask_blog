from Flask_blog.config_loader import load_environment_variables
from Flask_blog.database.db import Mongo

from os import environ


def test_connection():
    load_environment_variables()
    assert environ["MONGO_URI"]
    mongo_instance = Mongo(url=environ["MONGO_URI"], ServerSelectionTimeoutMS=5000)
    mongo_instance.find()
