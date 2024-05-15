from fastapi.routing import APIRouter

from ..db import DbSession
from .schemas import FeedbackIn, FeedbackOut
from .service import create

router = APIRouter(prefix="/feedbacks", tags=["feedbacks"])


@router.post("/", response_model=FeedbackOut, status_code=201)
async def create_feedback(db_session: DbSession, feedback: FeedbackIn):
    feedback_out = create(db_session, feedback)
    return feedback_out
