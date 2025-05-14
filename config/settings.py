import os

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    from dotenv import load_dotenv
    load_dotenv()

def str_list(value):
    return [v.strip() for v in value.split(",") if v.strip()]

class Settings:
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    CHAT_ID = os.getenv("CHAT_ID", "")
    KEYWORDS = str_list(os.getenv("KEYWORDS", "").lower())
    CHANNELS = str_list(os.getenv("CHANNELS", "").lower())

settings = Settings()