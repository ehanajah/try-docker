import os

env = os.getenv("APP_ENV", "development")

if env != "production":
    from dotenv import load_dotenv
    load_dotenv(".env")

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")
    