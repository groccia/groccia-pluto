from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class DBFeedback(Base):
    __tablename__ = "feedbacks"

    id = Column(UUID, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)
