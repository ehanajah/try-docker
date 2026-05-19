import os
from dotenv import load_dotenv

env = os.getenv("APP_ENV", "development")
print(env)

if env == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env")

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")
    