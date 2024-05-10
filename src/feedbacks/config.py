import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .constants import Constants


class Config:
    def __init__(self) -> None:
        self._credentials = self._get_credentials()
        self.service = self._get_google_service()

    @staticmethod
    def _get_credentials():
        credentials = None
        if os.path.exists(Constants.PATH_TO_TOKEN):
            credentials = Credentials.from_authorized_user_file(
                Constants.PATH_TO_TOKEN, Constants.SCOPES
            )
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    Constants.PATH_TO_CREDENTIALS, Constants.SCOPES
                )
                credentials = flow.run_local_server(port=0)
            with open(Constants.PATH_TO_TOKEN, "w") as token:
                token.write(credentials.to_json())

        return credentials

    def _get_google_service(self):
        try:
            service = build(
                serviceName=Constants.GOOGLE_SERVICE_NAME,
                version=Constants.GOOGLE_SERVICE_VERSION,
                credentials=self._credentials,
            )
        except Exception as error:
            print(f"An error occurred: {error}")
            raise error

        return service


config = Config()
