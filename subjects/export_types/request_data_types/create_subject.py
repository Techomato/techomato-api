from typing import Optional

from _decimal import Decimal
from pydantic import BaseModel


class CreateSubjectRequestType(BaseModel):
    courseName: str
    courseType: str
    courseCategory: str
    courseShortDescription: str
    course_price: Optional[Decimal] = 0.0
    courseFullDescription: Optional[str] = None
    image: Optional[str] = None
