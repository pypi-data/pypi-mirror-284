from dotenv import load_dotenv
import os

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_ENDPOINT = os.getenv("API_ENDPOINT") + "/v1/api"

if BEARER_TOKEN is None:
    raise SystemExit("BEARER_TOKEN is not set in the environment variables.")
if API_ENDPOINT is None:
    raise SystemExit("API_ENDPOINT is not set in the environment variables.")
