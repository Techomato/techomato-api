import typing
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from auth_api.export_types.user_types.export_user import ExportUser


class ExportReview(BaseModel):
    id: Optional[UUID]
    user: ExportUser
    text: Optional[str]
    rating: Optional[int]
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        if kwargs.get("user"):
            kwargs["user"] = ExportUser(**kwargs["user"].model_to_dict())
        super().__init__(**kwargs)


class ExportReviewList(BaseModel):
    review_list: typing.List[ExportReview]
