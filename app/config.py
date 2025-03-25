import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ["true", "1"]

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('DB_ENGINE')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_BINDS = {
        "read_replica": f"{os.getenv('DB_ENGINE')}://{os.getenv('READ_DB_USER')}:{os.getenv('READ_DB_PASSWORD')}@{os.getenv('READ_DB_HOST')}:{os.getenv('READ_DB_PORT')}/{os.getenv('READ_DB_NAME')}"
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security Config
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

