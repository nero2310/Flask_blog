import os.path
import json


class BaseConfig():
    def __init__(self, path):
        try:
            with open(path, "r") as file:
                self.configuration = json.load(path)
        except FileNotFoundError:
            self.configuration = {"user": "anon"}
