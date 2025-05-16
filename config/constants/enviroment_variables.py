from dotenv import load_dotenv
import os

load_dotenv()

# Constants for the bot configuration
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
BROWSER = os.getenv("BROWSER", "chrome").lower()
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER", "downloads")
BASE_URL = os.getenv("BASE_URL", required=True)