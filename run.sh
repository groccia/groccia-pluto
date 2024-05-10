#!bin/bash

# Start the API
poetry run uvicorn src.main:app --port 8686 --reload