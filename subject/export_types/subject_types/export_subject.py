from datetime import datetime
from typing import Optional, List
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser
from subject.export_types.subject_types.export_category import ExportCategory
from subject.export_types.subject_types.export_review import ExportReview


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
    review: Optional[List[ExportReview]] = None
    rating: Optional[int]
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_deleted: bool

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        if kwargs.get("author"):
            user_dict = kwargs["author"].model_to_dict()
            kwargs["author"] = ExportUser(**user_dict)
        if kwargs.get("courseCategory"):
            kwargs["courseCategory"] = ExportCategory(
                **kwargs["courseCategory"].model_to_dict()
            )
        if kwargs.get("review"):
            kwargs["review"] = [
                ExportReview(**review.model_to_dict())
                for review in kwargs["review"].all()
            ]
        super().__init__(**kwargs)


class ExportSubjectList(BaseModel):
    subject_list: List[ExportSubject]
