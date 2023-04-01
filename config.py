# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = 20804756
    API_HASH = "ecd0e2a4cc383ae5717059e7ae120adb"
    BOT_TOKEN = "5848693685:AAGRVeztgDyxHLCdP79Iu1rXZVvQmzXhfk0"
    LOGS_CHANNEL = "-1001552763930"
    MONGODB_URL = "mongodb+srv://mdmatinnew:Hg72p3iCsni9Olbf@cluster0.j2hvxhj.mongodb.net/?retryWrites=true&w=majority"
    BOT_OWNER = "5576458964"
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2040108421
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 6
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
