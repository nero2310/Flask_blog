import pytest

from flask import session
from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.testing = True
    app.test_client()
    return app


def test_basic(client):
    client = client.test_client()
    client.get("/")


def test_create_post(client):
    with client.test_client() as context:
        assert context.post("/post/create", data="")
        session["username"] = "test_user"
