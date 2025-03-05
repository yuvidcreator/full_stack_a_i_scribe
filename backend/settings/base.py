import pytz, os
from typing import List
from pydantic_settings import BaseSettings
# from pydantic import EmailStr, Field,  AnyHttpUrl
from dotenv import load_dotenv
from datetime import datetime, timezone


load_dotenv()

asia_timezone = pytz.timezone('Asia/Kolkata')


def current_datetime() -> datetime:
    return datetime.now(asia_timezone)


class Settings(BaseSettings):
    SECRET_KEY: str

    ENV: str
    DEBUG: bool

    CLIENT_ORIGIN: str
    ALLOWED_ORIGIN: List[str] = os.getenv('CLIENT_ORIGIN', cast=str).split()

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    S3_BUCKET_NAME: str
    S3_REGION: str

    OPENAI_API_KEY: str

    # POSTGRES_DB: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_HOST: str
    # POSTGRES_PORT: str

    DATABASE_URL: str

    # SQLALCHEMY_DATABASE_URL_LOCAL: AnyHttpUrl = Field(
    #     "sqlite:///db.sqlite", validate_default=False)

    # SQLALCHEMY_DATABASE_URL_DEV: AnyHttpUrl = Field(
    #     sa.URL.create(
    #         drivername="postgresql+psycopg2",
    #         username=config("POSTGRES_USER"),
    #         password=config("POSTGRES_PASSWORD"),
    #         host=config("POSTGRES_HOST"),
    #         port=config("POSTGRES_PORT"),
    #         database=config("POSTGRES_DB"),
    #     ), validate_default=False
    # )

    # SQLALCHEMY_DATABASE_URL_PROD: AnyHttpUrl = Field(
    #     sa.URL.create(
    #         drivername="postgresql+psycopg2",
    #         username=config("POSTGRES_USER"),
    #         password=config("POSTGRES_PASSWORD"),
    #         host=config("POSTGRES_HOST"),
    #         port=config("POSTGRES_PORT"),
    #         database=config("POSTGRES_DB"),
    #     ),
    #     validate_default=False
    # )

    # REDIS_HOST: str
    # REDIS_PORT: int
    # REDIS_DB: int

    # REDIS_BROKER_URL: str = Field(
    #     config('REDIS_BROKER_URL', cast=str, default="redis://localhost:6379/0"))
    # REDIS_BACKEND_URL: str = Field(
    #     config('REDIS_BACKEND_URL', cast=str, default="redis://localhost:6379/0"))

    # # Elastic search
    # ELASTICSEARCH_HOSTS: str

    class Config:
        env_file = '.env'


settings = Settings()
