from typing import Optional

from psycopg2 import DatabaseError

from subjects.export_types.request_data_types.create_subject import (
    CreateSubjectRequestType,
)
from subjects.export_types.subject_types.export_subject import ExportSubject, ExportSubjectList
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

    @staticmethod
    def get_all_subjects_service() -> Optional[ExportSubjectList]:
        try:
            subjects = Subject.objects.all()
        except Exception:
            raise DatabaseError()
        if subjects:
            all_subjects_details = []
            for subject in subjects:
                all_subjects_details = ExportSubject(**subject.model_to_dict())
                # all_subjects_details = ExportSubject(with_id=False, **user.model_to_dict())
                all_subjects_details.append(all_subjects_details)
            all_subject = ExportSubjectList(subject_list=all_subjects_details)
            return all_subject
        else:
            return None
