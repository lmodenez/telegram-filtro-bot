import os

if not os.getenv("RAILWAY_ENVIRONMENT"):
    from dotenv import load_dotenv
    load_dotenv()

def str_list(value):
    return [v.strip() for v in value.split(",") if v.strip()]

class Settings:
    def __init__(self):
        self.API_ID = int(os.getenv("API_ID", 0))
        self.API_HASH = os.getenv("API_HASH", "")
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.CHAT_ID = os.getenv("CHAT_ID", "")
        self.KEYWORDS = str_list(os.getenv("KEYWORDS", "").lower())
        self.CHANNELS = str_list(os.getenv("CHANNELS", "").lower())

        self.validate()

    def validate(self):
        if not self.API_ID or not self.API_HASH:
            raise ValueError("API_ID and API_HASH must be set")

settings = Settings()