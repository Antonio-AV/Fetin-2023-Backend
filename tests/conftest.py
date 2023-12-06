# tests/conftest.py
import pytest
import config
from api.api import app


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client
