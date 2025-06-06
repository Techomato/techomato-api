from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_api.services.handlers.exception_handlers import ExceptionHandler
from auth_api.services.helpers import decode_jwt_token, validate_user_uid
from subject.export_types.subject_types.export_enrollments import (
    ExportEnrollmentSubjectList,
)
from subject.services.subject_services import SubjectServices


class AllEnrolledSubjectView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                all_enrolled_subjects = (
                    SubjectServices.get_all_enrolled_subjects_service(user_id=user_id)
                )
                if all_enrolled_subjects and isinstance(
                    all_enrolled_subjects, ExportEnrollmentSubjectList
                ):
                    return Response(
                        data={
                            "data": all_enrolled_subjects.model_dump(),
                            "message": "Get all enrolled subjects successfully.",
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    return Response(
                        data={
                            "data": {"enrollment_subject_list": []},
                            "message": "No data found in database.",
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
