from typing import Optional

from pydantic import BaseModel


class EditSubjectRequestType(BaseModel):
    id: Optional[str] = None
    courseShortDescription: Optional[str] = None
    courseFullDescription: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    image: Optional[str] = None
