from subjects.export_types.request_data_types.create_subject import (
    CreateSubjectRequestType,
)
from subjects.export_types.subject_types.export_subject import ExportSubject
from subjects.models.subject import Subject
from subjects.serializers.subject_serializer import SubjectSerializer


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
