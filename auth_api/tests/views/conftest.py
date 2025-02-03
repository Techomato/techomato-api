import pytest

from auth_api.models.user_models.user import User


@pytest.fixture
def user_list():
    return [
        {
            "id": "a0309afd-2f4a-4726-9903-fb07e3d7500e",
            "username": "koushikmallik",
            "email": "koushikmallik001@gmail.com",
            "name": "Koushik Mallik",
            "account_type": "regular",
            "dob": None,
            "phone": None,
            "password": "b'gAAAAABlcLJF0FLjcCWFUWQfRl442eAlZ9_IGgfUJAHlXpinOI_YrnpfUtXBfKpJifVI9T9JNuSUy9ax3oCyLbbqouA8rjd9Lg=='",  # pragma: allowlist-secret # noqa
            "image": "/images/users/defaultUserImage.png",
            "is_active": True,
            "is_deleted": False,
            "is_admin": False,
            "is_staff": False,
        },
        {
            "id": "8a3a52ad-bb84-425c-bda7-884effd28374",
            "username": "koushikmallik1",
            "email": "animeshece1998@gmail.com",
            "name": "Koushik Google",
            "password": "b'gAAAAABlcLJF0FLjcCWFUWQfRl442eAlZ9_IGgfUJAHlXpinOI_YrnpfUtXBfKpJifVI9T9JNuSUy9ax3oCyLbbqouA8rjd9Lg=='",  # pragma: allowlist-secret # noqa
            "account_type": "regular",
            "dob": None,
            "phone": None,
            "image": "/images/users/defaultUserImage.png",
            "is_active": False,
            "is_deleted": False,
            "is_admin": False,
            "is_staff": False,
        },
    ]


@pytest.fixture
def create_test_user(user_list):
    for user in user_list:
        User(**user).save()


@pytest.fixture
def empty_database(user_list):
    User.objects.all().delete()


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def access_token(api_client):
    signin_data = {
        "email": "koushikmallik001@gmail.com",
        "password": "1234567",  # pragma: allowlist-secret # noqa
    }

    response = api_client.post(
        "http://localhost:8000/api/auth/sign-in", signin_data, format="json"
    )
    response = response.json()
    if "token" not in response:
        raise ValueError("Token not found in response")
    token = response["token"]["access"]
    return token
