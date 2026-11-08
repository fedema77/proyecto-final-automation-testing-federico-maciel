import requests
import pytest

BASE_URL = "https://reqres.in/api"


def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=2", timeout=10)

    assert response.status_code == 200
    payload = response.json()
    assert "data" in payload
    assert len(payload["data"]) > 0
    assert "email" in payload["data"][0]


def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2", timeout=10)

    assert response.status_code == 204
    assert response.text == ""
