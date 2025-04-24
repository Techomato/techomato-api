import typing
from datetime import datetime
from typing import Optional
from uuid import UUID


from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser
from auth_api.models.user_models.user import User
from subject.export_types.subject_types.export_subject import ExportSubjectList


class ExportEnrollment(BaseModel):
    id: Optional[UUID]
    student: ExportUser
    course: ExportSubjectList
    enrolled_at: datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        if isinstance(kwargs["user"], User):
            user_dict = kwargs["user"].model_to_dict()
            kwargs["user"] = ExportUser(**user_dict)
        if "course" in kwargs and isinstance(kwargs["course"], list):
            kwargs["course"] = ExportSubjectList(subject_list=kwargs["course"])

        super().__init__(**kwargs)


class ExportEnrollmentSubjectList(BaseModel):
    subject_list: typing.List[ExportEnrollment]
