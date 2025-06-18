import os

from dotenv import load_dotenv

from yt import connectYouTube
from db import get_database

load_dotenv()
key = os.getenv("API_KEY")
if key:
    yt = connectYouTube(key)
else:
    print("Chave API não encontrada")
    
mongo = get_database()["youtube"]
mongo.list_collection_names()