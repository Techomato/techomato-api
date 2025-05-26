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
    student: ExportUser
    course: ExportSubjectList
    enrolled_at: datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        if isinstance(kwargs.get("user")):
            kwargs["user"] = ExportUser(**kwargs.get("user"))
        if "subject" in kwargs:
            kwargs["course"] = ExportSubjectList(
                subject_list=[
                    ExportSubject(**subject.model_to_dict())
                    for subject in kwargs["subject"].all()
                ]
            )

        super().__init__(**kwargs)


class ExportEnrollmentSubjectList(BaseModel):
    subject_list: typing.List[ExportEnrollment]
