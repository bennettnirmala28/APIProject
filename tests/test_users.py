import pytest
from utils.api_client import APIClient
from utils.test_data import NEW_USER, UPDATED_USER
 

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_user(api_client):
    response = api_client.get("users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_create_user(api_client):
    response = api_client.post("users", data=NEW_USER)
    assert response.status_code == 201
    assert response.json()["name"] == NEW_USER["name"]
 
def test_update_user(api_client):
    response = api_client.put("users/2", data=UPDATED_USER)
    assert response.status_code == 200
    assert response.json()["job"] == UPDATED_USER["job"]

def test_delete_user(api_client):
    response = api_client.delete("users/2")
    assert response.status_code == 204

    