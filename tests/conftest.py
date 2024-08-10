import pytest
from fastapi.testclient import TestClient

import src.main

@pytest.fixture
def set_env_var(monkeypatch):
    monkeypatch.setenv("test", "new_value")
    yield

@pytest.fixture
def default_client():
    return TestClient(src.main.app)