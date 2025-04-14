import typing
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser
from subject.models.review import Review


class ExportReview(BaseModel):
    id: Optional[UUID]
    user: ExportUser
    text: Optional[str]
    rating: Optional[int]
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        if kwargs["review"] and isinstance(kwargs["review"], Review):
            kwargs["review"] = ExportReview(**kwargs["review"].model_to_dict())
        super().__init__(**kwargs)


class ExportReviewList(BaseModel):
    group_list: typing.List[ExportReview]
