from pathlib import Path

ASSETS = Path(__file__).parent / "assets"
LOG_FILE = ASSETS / "log" / "app.log"
DATA_FILE = ASSETS / "resources" / "data.csv"
LOGO_FILE = ASSETS / "images" / "logo1.svg"

# Define the App routes
HOME_ROUTE = "/"
DICTIONARY_ROUTE = "/dictionary"
ABOUT_ROUTE = "/about"
API_DOCS_ROUTE = "/api-docs"

# Define the API routes
BASE_URL = "http://127.0.0.1:8080"
WORDWIZ_API_ROUTE = '/wordwiz-api/v1/define'

# Define minimum word input length requirement in the webapp 
MIN_INPUT_LENGTH = 3  