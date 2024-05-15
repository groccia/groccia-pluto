import uuid

from .models import DBFeedback
from .schemas import FeedbackIn


def create(db_session, feedback_in: FeedbackIn) -> DBFeedback:
    db_feedback = DBFeedback(**feedback_in.model_dump(), id=uuid.uuid4())

    db_session.add(db_feedback)
    db_session.commit()
    return db_feedback
