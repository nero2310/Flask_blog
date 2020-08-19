from sys import exit
import os.path

from dotenv import load_dotenv


def create_base_config(path):
    """Create configuration file
    :arg path path to config file
    """
    if os.path.isfile(path):
        print("Config file already exist")
        exit(0)
    else:
        config = f"secret_key={os.urandom(20).hex()}\n" \
                 f"env=production\n" \
                 f"MONGO_URI='paste adress of your database here'"
        with open(path, "w") as file:
            file.write(config)


def load_environment_variables(path_to_file=".env"):
    """ :arg path_to_file load environment variables from file """
    try:
        load_dotenv(dotenv_path=path_to_file)
    except FileExistsError:
        raise FileExistsError("Environment file not found")

if __name__ == "__main__":
    create_base_config(".env")
