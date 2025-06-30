import os
from pathlib import Path

from dotenv import load_dotenv

from db import get_database
from yt import *

load_dotenv()
key = os.getenv("API_KEY")
if key:
    yt = connectYouTube(key)
else:
    print("Chave API não encontrada")
    
db = get_database()["youtube"]
dbVideos = db["videos"]
dbComments = db["comments"]
dbTranscriptions = db["transcriptions"]
dbLivechats = db["livechats"]
dbSuperchats = db["superchats"]

channel_url = input("Insira URL do canal: ")
channel_id = yt.channel_id_from_url(channel_url)

def getUploadedVideosId(channelId: str) -> list[str]:
    videos = []
    assert channelId[:2] == "UC"
    print("Procurando os 10 últimos videos...")
    for index, video in enumerate(yt.playlist_videos("UU" + channelId[2:])):
        videos.append(video["id"]) # type: ignore
        if index == 9:
            break
    return videos

if channel_id:
    videos = getUploadedVideosId(channelId=channel_id)
    videos_info = yt.videos_infos(videos)
    dbVideos.insert_many(videos_info)

    for id in videos:
        for comment in getComments(yt, id):
            dbComments.insert_one(comment)
    print("Comentários salvos")
    
    for chat in yt.video_livechat('fkyZFWKY9Eo'):
        if chat["money_amount"] == None:
            dbLivechats.insert_one(chat)
        else:
            chat["money_amount"] = float(chat["money_amount"])
            dbSuperchats.insert_one(chat)
    print("Superchats salvos")

    download_path = Path("transcriptions")
    if not download_path.exists():
        download_path.mkdir(parents=True)

    print(f"Baixando transcrições em Português (pt) de {videos} em:  {download_path.absolute()}")

    for video in videos:
        try:
            [res] = yt.download_transcriptions(videos_ids=[video],language_code="pt",path=download_path)
            vid = res["video_id"]
            status = res["status"]
            filename = res["filename"]

            if status == "error":
                print(f"  {vid}: erro no download!")
            elif status == "skipped":
                if filename is not None and filename.exists():
                    size_kib = filename.stat().st_size / 1024
                    print(f"  {vid}: pulado, arquivo já existe ({filename.name}: {size_kib:.1f} KiB)")
                else:
                    print(f"  {vid}: pulado, arquivo já existe (mas não consegui ler o tamanho)")
            elif status == "done":
                size_kib   = filename.stat().st_size / 1024
                print(f"  {vid}: pronto ({filename.name}: {size_kib:.1f} KiB)")
                full_text  = filename.read_text(encoding="utf-8")
                doc = {
                    "_id":      f"{vid}_pt",
                    "video_id": vid,
                    "language": "pt",
                    "text":     full_text,
                    "size":     filename.stat().st_size,
                }
                dbTranscriptions.replace_one({"_id": doc["_id"]}, doc, upsert=True)
        except Exception as e:
            print(f"{vid}: pulado – {e}")