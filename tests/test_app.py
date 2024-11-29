import pytest
from awesome_api import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to Awesome API!"
