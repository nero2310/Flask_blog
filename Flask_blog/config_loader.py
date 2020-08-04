import os.path
from dotenv import load_dotenv
from os import environ

from json import dump, load


def create_base_config(path):
    config = f"secret_key={os.urandom(20).hex()}\n" \
             f"env=production"
    with open(path, "w") as file:
        file.write(config)


def load_environment_variables(path=".env"):
    try:
        load_dotenv(dotenv_path=path)
    except:
        raise FileExistsError("Environment file not found")
