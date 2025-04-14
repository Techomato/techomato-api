from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_api.services.handlers.exception_handlers import ExceptionHandler
from subject.export_types.subject_types.export_subject import ExportSubjectList
from subject.services.subject_services import SubjectServices


class AllSubjectsView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, _):
        try:
            all_subjects = SubjectServices.get_all_subjects_service()
            if all_subjects and isinstance(all_subjects, ExportSubjectList):
                return Response(
                    data={
                        "data": all_subjects.model_dump(),
                        "message": None,
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                return Response(
                    data={
                        "data": {"user_list": []},
                        "message": "No User found in database.",
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
