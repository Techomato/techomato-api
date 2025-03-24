from __future__ import annotations
import datetime
import typing
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ExportUser(BaseModel):
    id: Optional[UUID]
    email: str
    name: str
    username: Optional[str] = None
    account_type: Optional[str] = None
    dob: Optional[datetime.datetime] = None
    phone: Optional[str] = None
    image: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    is_admin: Optional[bool] = None
    is_staff: Optional[bool] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportUserList(BaseModel):
    user_list: typing.List[ExportUser]
