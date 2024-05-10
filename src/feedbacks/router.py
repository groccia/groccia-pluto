from fastapi.routing import APIRouter

from .schemas import FeedbackIn, FeedbackOut
from .service import FeedbackService

router = APIRouter()

feedback_service = FeedbackService()


@router.post("/feedbacks/", response_model=FeedbackOut, status_code=201)
async def create_feedback(feedback: FeedbackIn):
    feedback_out = feedback_service.create_feedback(feedback)
    return feedback_out
