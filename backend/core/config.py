import os

from dotenv import load_dotenv

# env_path = Path('.') / '.env'
load_dotenv()


class Settings:
    PROJECT_NAME: str = "Mondongo"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_SERVER: str = os.getenv("DATABASE_SERVER", "localhost")
    DATABASE_PORT: str = os.getenv(
        "DATABASE_PORT", 5432
    )  # default POSTGRES port is 5432
    DATABASE_DB: str = os.getenv("DATABASE_DB", "tdd")
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_DB}"
    if os.getenv("ENVIRONMENT") == "development":
        DATABASE_URL = "sqlite:///./sql_app.db"


settings = Settings()
