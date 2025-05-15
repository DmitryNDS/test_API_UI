from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    API_BASE_URL: str = os.getenv("API_BASE_URL", "")
    UI_BASE_URL: str = os.getenv("UI_BASE_URL", "")
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT: int = int(os.getenv("IMPLICIT_WAIT", "10"))
    PAGE_LOAD_TIMEOUT: int = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 