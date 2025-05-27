from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Browser settings
    BROWSER: str = "chrome"
    HEADLESS: bool = False
    
    # Timeouts
    IMPLICIT_WAIT: int = 10
    PAGE_LOAD_TIMEOUT: int = 30
    SCRIPT_TIMEOUT: int = 30
    
    # URLs
    BASE_URL: str = "https://automationexercise.com"
    
    # Test data
    TEST_USER_EMAIL: str = "test@example.com"
    TEST_USER_PASSWORD: str = "password123"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 