# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get ("15236804"))
    API_HASH = os.environ.get("409da5b68ad699091fa72b381921f0e5")
    BOT_TOKEN = os.environ.get("5612635073:AAF03jY6fawSLM9BGYpNB8_JKdnDlgyr-qs")
    LOGS_CHANNEL = int(os.environ.get("-1001684353224"))
    MONGODB_URL = os.environ.get("mongodb+srv://mdmatinnew:Hg72p3iCsni9Olbf@cluster0.j2hvxhj.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("1963114305"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2040108421
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 6
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
