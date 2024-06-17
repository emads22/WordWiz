import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

ASSETS = Path(__file__).parent / "assets"
LOGS = ASSETS / "log"
RESOURCES = ASSETS / "resources"
LOG_FILE = LOGS / "app.log"
DATA_FILE = RESOURCES / "data.csv"



