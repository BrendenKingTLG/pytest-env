from fastapi.testclient import TestClient

import src.main

def test_default_env_var(default_client):
    response = default_client.get("/")
    assert response.json() == {"var": "default"}


def test_modified_env_var(reload_client_with_var):
    client = reload_client_with_var("test", "example")
    response = client.get("/")
    assert response.json() == {"var": "example"}
    
def test_default_env_var2(default_client):
    response = default_client.get("/")
    assert response.json() == {"var": "default"}