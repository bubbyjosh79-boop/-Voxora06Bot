import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "voxora.db")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Railway URL
    PORT = int(os.getenv("PORT", 8080))
