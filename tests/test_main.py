import importlib
from fastapi.testclient import TestClient

import src.main

def test_default_env_var(default_client):
    response = default_client.get("/")
    assert response.json() == {"var": "default"}


def test_modified_env_var(set_env_var):
    importlib.reload(src.main)
    client = TestClient(src.main.app)
    response = client.get("/")
    assert response.json() == {"var": "new_value"}