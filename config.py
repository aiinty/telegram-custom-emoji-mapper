import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Telegram credentials ---
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Data save paths ---
SESSION = os.path.join(BASE_DIR, os.getenv("SESSION"))
DOWNLOAD_DIR = os.path.join(BASE_DIR, os.getenv("DOWNLOAD_DIR"))