from typing import Optional

from psycopg2 import DatabaseError

from auth_api.models.user_models.user import User
from subjects.exceptions.subject_exceptions import PermissionDeniedError, SubjectNotFoundError
from subjects.export_types.request_data_types.create_subject import (
    CreateSubjectRequestType,
)
from subjects.export_types.request_data_types.edit_subject import EditSubjectRequestType
from subjects.export_types.subject_types.export_subject import (
    ExportSubject,
    ExportSubjectList,
)
from subjects.models.subject import Subject
from subjects.serializers.subject_serializer import SubjectSerializer

from django.utils import timezone


class SubjectServices:
    @staticmethod
    def create_new_subject_service(
        request_data: CreateSubjectRequestType, uid: str
    ) -> dict:
        data: dict = {"request_data": request_data, "uid": uid}
        subject: Subject = SubjectSerializer().create(data)
        return {
            "message": f"{subject.courseName} is created",
            "data": ExportSubject(**subject.model_to_dict()).model_dump(),
        }

    @staticmethod
    def get_all_subjects_service() -> Optional[ExportSubjectList]:
        try:
            subjects = Subject.objects.all()
        except Exception:
            raise DatabaseError()
        if subjects:
            all_subject = ExportSubjectList(
                subject_list=[
                    ExportSubject(with_id=False, **subject.model_to_dict())
                    for subject in subjects
                ]
            )
            return all_subject
        else:
            return None

    @staticmethod
    def edit_subject(uid: str, request_data: EditSubjectRequestType) -> ExportSubject:
        user = User.objects.get(id=uid, is_deleted=False)
        if not user.is_admin:
            raise NotAllowedEditSubjectError()

        subject = Subject.objects.get(id=request_data.id, is_deleted=False)
        if not subject:
            raise SubjectNotFoundError()
        if str(subject.author.id) != str(uid):
            raise NotAllowedEditSubjectError()

        if (
            request_data.image
            and isinstance(request_data.image, str)
            and request_data.image != ""
            and request_data.image != subject.image
        ):
            subject.image = request_data.image
        if (
            request_data.courseFullDescription
            and isinstance(request_data.courseFullDescription, str)
            and request_data.courseFullDescription != ""
            and request_data.courseFullDescription != subject.courseFullDescription
        ):
            subject.courseFullDescription = request_data.courseFullDescription
        if (
            request_data.courseShortDescription
            and isinstance(request_data.courseShortDescription, str)
            and request_data.courseShortDescription != ""
            and request_data.courseShortDescription != subject.courseShortDescription
        ):
            subject.courseShortDescription = request_data.courseShortDescription
        if (
            request_data.is_active
            and isinstance(request_data.is_active, bool)
            and request_data.is_active != subject.is_active
        ):
            subject.is_active = request_data.is_active
        if (
            request_data.is_deleted
            and isinstance(request_data.is_deleted, bool)
            and request_data.is_deleted != subject.is_deleted
        ):
            subject.is_deleted = request_data.is_deleted

        subject.updated_at = timezone.now()
        subject.save()
        return ExportSubject(**subject.model_to_dict())
