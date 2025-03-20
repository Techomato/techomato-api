import typing
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ExportCategory(BaseModel):
    id: Optional[UUID]
    name: str


class ExportCategoryList(BaseModel):
    group_list: typing.List[ExportCategory]
