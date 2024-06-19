from pathlib import Path

ASSETS = Path(__file__).parent / "assets"
LOGS = ASSETS / "log"
RESOURCES = ASSETS / "resources"
IMAGES = ASSETS / "images"
LOG_FILE = LOGS / "app.log"
DATA_FILE = RESOURCES / "data.csv"
LOGO_FILE = IMAGES / "logo1.svg"