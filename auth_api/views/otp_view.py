from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_api import executor
from auth_api.auth_exceptions.user_exceptions import (
    UserAlreadyVerifiedError,
    UserNotFoundError,
)
from auth_api.models.user_models.user import User
from auth_api.services.definitions import DEFAULT_VERIFICATION_MESSAGE
from auth_api.services.handlers.exception_handlers import ExceptionHandler
from auth_api.services.helpers import validate_user_email
from auth_api.services.otp_services.otp_services import OTPServices


class SendOTPView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request: Request):
        try:
            request_data = request.data
            email = request_data.get("email")
            if email and validate_user_email(email).is_validated:
                user = User.objects.get(email=email)
                if not user.is_active:
                    executor.submit(OTPServices().send_otp_to_user, user.email)
                    return Response(
                        data={
                            "message": DEFAULT_VERIFICATION_MESSAGE,
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    raise UserAlreadyVerifiedError()
            else:
                raise UserNotFoundError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
