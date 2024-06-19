from pathlib import Path

ASSETS = Path(__file__).parent / "assets"
LOGS = ASSETS / "log"
RESOURCES = ASSETS / "resources"
IMAGES = ASSETS / "images"
LOG_FILE = LOGS / "app.log"
DATA_FILE = RESOURCES / "data.csv"
LOGO_FILE = IMAGES / "logo1.svg"

# Define the API routes
BASE_URL = "http://127.0.0.1:8080"
WORDWIZ_API_ROUTE = '/api/v1/dictionary'
