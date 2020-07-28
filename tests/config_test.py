from Flask_blog.config_loader import BaseConfig
import pytest


def test_base_conf(tmp_path):  # get_secret_key shoudln't casue exception
    path = tmp_path / "test_dir"
    path.mkdir()
    config = BaseConfig(path / "config.json")
    assert config.get_secret_key()
