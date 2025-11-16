import pytest
from api import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    with app.test_client() as flask_client:
        yield flask_client
