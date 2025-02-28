import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from auth_api.models.user_models.user import User
from auth_api.services.helpers import decode_jwt_token


@pytest.mark.usefixtures("create_test_user")
@pytest.mark.django_db
class TestRemoveUserView:
    url = "/api/auth/remove-user"

    def test_remove_user_success(self, api_client: APIClient, access_token: str):
        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
        }
        response = api_client.post(self.url, headers=headers, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "User removed Successfully."

        token = AccessToken(access_token)
        payload = token.payload
        user_id = payload.get("user_id")
        user = User.objects.get(id=user_id)
        assert user.is_deleted is True

    def test_remove_user_unauthorized(self, api_client: APIClient):
        headers = {
            "Content-Type": "application/json",
        }
        response = api_client.post(self.url, headers=headers, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert (
            response.data["message"]
            == "UserNotAuthenticatedError: The user is not authenticated, please re-login."
        )
