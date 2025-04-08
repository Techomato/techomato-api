from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_api.services.handlers.exception_handlers import ExceptionHandler
from auth_api.services.user_services.user_services import UserServices


class LogoutView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            UserServices.logout_user(request)
            return Response(
                data={"message": "User logged out successfully."},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
