
import os
from datetime import datetime, timezone
from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    raise RuntimeError(
        "MONGODB_URI set nahi hai. Project ki .env file check karo."
    )

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["instasocial"]
collection = db["instagram_public_profiles"]


def save_username(username,password):
    username = username.strip().lstrip("@")
    password = password.strip()

    collection.insert_one({
        "platform": "instagram",
        "username": username,
        "password": password,
        "created_at": datetime.now(timezone.utc)
    })

    return True, "Username MongoDB mein save ho gaya."
