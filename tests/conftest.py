import pytest
from items_api import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
