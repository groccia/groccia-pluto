from fastapi import FastAPI

from src.config import settings
from src.feedbacks.router import router as feedback_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(feedback_router, prefix=settings.API_V1_STR)
