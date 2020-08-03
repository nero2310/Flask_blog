import os.path
from json import dump,load


def create_base_config(path):
    config = {
        "secret_key": os.urandom(20).hex()
    }
    with open(path, "w") as file:
       dump(config,file)
    return config


class BaseConfig:
    def __init__(self, path):
        try:
            with open(path, "r") as file:
                self.configuration = load(file)
        except FileNotFoundError:
            self.configuration = create_base_config(path)

    def get_secret_key(self):
        return self.configuration["secret_key"]
