import typing
from datetime import datetime
from typing import Optional
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser
from auth_api.models.user_models.user import User
from subjects.export_types.subject_types.export_category import ExportCategory
from subjects.export_types.subject_types.export_review import ExportReview
from subjects.models.category import Category


class ExportSubject(BaseModel):
    id: Optional[UUID]
    author: ExportUser
    courseName: str
    courseType: str
    price: Decimal
    courseCategory: ExportCategory
    courseShortDescription: str
    courseFullDescription: Optional[str]
    image: Optional[str]
    review: Optional[ExportReview] = None
    rating: Optional[int]
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_deleted: bool

    def __init__(self, **kwargs):
        if isinstance(kwargs["author"], User):
            kwargs["author"] = ExportUser(**kwargs["author"].model_to_dict())
        if isinstance(kwargs["courseCategory"], Category):
            kwargs["courseCategory"] = ExportCategory(
                **kwargs["courseCategory"].model_to_dict()
            )
        super().__init__(**kwargs)


class ExportSubjectList(BaseModel):
    subject_list: typing.List[ExportSubject]
