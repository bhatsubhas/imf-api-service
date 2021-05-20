import pytest
from api.app import app


@pytest.fixture
def client():
    with app.test_client() as flask_client:
        yield flask_client
