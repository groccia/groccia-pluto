from googleapiclient.errors import HttpError

from .config import config
from .constants import Constants
from .schemas import FeedbackIn, FeedbackOut


class FeedbackService:
    def __init__(self) -> None:
        self._service = config.service

    def create_feedback(self, feedback: FeedbackIn) -> FeedbackOut:
        feedback_out = FeedbackOut(**feedback.model_dump())

        values = [
            (
                feedback_out.id,
                feedback_out.created_at.isoformat(),
                feedback_out.email,
                feedback_out.message,
            )
        ]
        body = {"values": values}

        # Add feedback to Google Sheets
        try:
            result = (
                self._service.spreadsheets()
                .values()
                .append(
                    spreadsheetId=Constants.SPREADSHEET_ID,
                    range=Constants.RANGE_NAME,
                    valueInputOption=Constants.VALUE_INPUT_OPTION,
                    body=body,
                )
                .execute()
            )
            print(f"{(result.get('updates').get('updatedCells'))} cells appended.")

        except HttpError as error:
            print(f"An error occurred: {error}")
            raise error

        return feedback_out
