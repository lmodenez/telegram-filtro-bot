import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    KEYWORDS = [k.strip().lower() for k in os.getenv("KEYWORDS", "").split(",")]
    CHANNELS = [c.strip().lower() for c in os.getenv("CHANNELS", "").split(",")]

settings = Settings()