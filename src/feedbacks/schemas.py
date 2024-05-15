from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class FeedbackIn(BaseModel):
    email: EmailStr
    message: str


class FeedbackOut(FeedbackIn):
    id: UUID
    created_at: datetime
