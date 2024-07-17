import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")


settings = Settings()
