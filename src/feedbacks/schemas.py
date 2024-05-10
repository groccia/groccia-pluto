from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class FeedbackIn(BaseModel):
    email: EmailStr
    message: str


class FeedbackOut(FeedbackIn):
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)
