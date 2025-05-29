import typing
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser
from subject.export_types.subject_types.export_subject import (
    ExportSubjectList,
    ExportSubject,
)


class ExportEnrollment(BaseModel):
    id: Optional[UUID]
    user: Optional[ExportUser] = None
    subjects: Optional[ExportSubjectList] = None
    enrolled_at: datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        if kwargs.get("user"):
            kwargs["user"] = ExportUser(**kwargs.get("user").model_to_dict())
        if (
            "subjects" in kwargs
            and kwargs["subjects"].all()
            and len(kwargs["subjects"].all())
        ):
            kwargs["subjects"] = ExportSubjectList(
                subject_list=[
                    ExportSubject(**subject.model_to_dict())
                    for subject in kwargs["subjects"].all()
                ]
            )

        super().__init__(**kwargs)


class ExportEnrollmentSubjectList(BaseModel):
    subject_list: typing.List[ExportEnrollment]
