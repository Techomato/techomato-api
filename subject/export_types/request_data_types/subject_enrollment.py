from typing import Optional

from pydantic import BaseModel


class EnrollSubjectRequestType(BaseModel):
    subject_id: Optional[str] = None
