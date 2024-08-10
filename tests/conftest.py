import pytest
from fastapi.testclient import TestClient
import importlib

import src.main

@pytest.fixture
def reload_client_with_var(monkeypatch):
    def reloaded_client(key, value):
        monkeypatch.setenv(key, value)
        importlib.reload(src.main)
        return TestClient(src.main.app)

    return reloaded_client

@pytest.fixture
def default_client():
    importlib.reload(src.main)
    return TestClient(src.main.app)