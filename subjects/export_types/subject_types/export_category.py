import typing
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from subjects.models.category import Category


class ExportCategory(BaseModel):
    id: Optional[UUID]
    name: str

    def __init__(self, **kwargs):
        category = kwargs.get("category")
        if category and isinstance(category, Category):
            kwargs["category"] = ExportCategory(**category.model_to_dict())
        super().__init__(**kwargs)


class ExportCategoryList(BaseModel):
    group_list: typing.List[ExportCategory]
