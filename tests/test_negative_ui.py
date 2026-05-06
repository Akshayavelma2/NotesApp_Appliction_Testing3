import requests
from config.environment import config
from api.api_client import APIClient


def get_auth_headers():
    api = APIClient()
    api.login()

    return {
        "x-auth-token": api.token
    }


def test_api_login_invalid_password():

    url = f'{config["api_url"]}/users/login'

    payload = {
        "email": config["email"],
        "password": "wrong_password"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [400, 401]


def test_api_login_invalid_email():

    url = f'{config["api_url"]}/users/login'

    payload = {
        "email": "wrongemail@gmail.com",
        "password": "wrongpassword"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [400, 401]


def test_create_note_without_title():

    payload = {
        "description": "Missing title",
        "category": "Home"
    }

    response = requests.post(
        f'{config["api_url"]}/notes',
        json=payload,
        headers=get_auth_headers()
    )

    assert response.status_code in [400, 422]


def test_create_note_without_description():

    payload = {
        "title": "Missing Description",
        "category": "Home"
    }

    response = requests.post(
        f'{config["api_url"]}/notes',
        json=payload,
        headers=get_auth_headers()
    )

    assert response.status_code in [400, 422]


