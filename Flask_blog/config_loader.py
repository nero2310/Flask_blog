import os.path

from dotenv import load_dotenv


def create_base_config(path):
    """Create configuration file
    :arg path path to config file
    """
    config = f"secret_key={os.urandom(20).hex()}\n" \
             f"env=production"
    with open(path, "w") as file:
        file.write(config)


def load_environment_variables(path_to_file=".env"):
    """ :arg path_to_file load environment variables from file """
    try:
        load_dotenv(dotenv_path=path_to_file)
    except FileExistsError:
        raise FileExistsError("Environment file not found")
