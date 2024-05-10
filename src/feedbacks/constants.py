class Constants:
    SPREADSHEET_ID = "1cSt5hp63PIV3Qu0cRrdrQhBNVHy2mJZPO0dLeAosnV0"
    VALUE_INPUT_OPTION = "USER_ENTERED"
    SHEET_NAME = "CustomerFeedback"
    START_CELL = "A1"
    END_CELL = "D1"
    RANGE_NAME = f"{SHEET_NAME}!{START_CELL}:{END_CELL}"

    GOOGLE_SERVICE_NAME = "sheets"
    GOOGLE_SERVICE_VERSION = "v4"

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    PATH_TO_TOKEN = "env/token.json"
    PATH_TO_CREDENTIALS = "env/credentials.json"
