from Flask_blog.config_loader import load_environment_variables
from pytest import raises

from os import environ


def test_env_variables():
    load_environment_variables()
    assert environ["env"]
    assert environ["secret_key"]
    with raises(KeyError):
        assert environ["random_word_blalalla"]  # check if exception is raised
