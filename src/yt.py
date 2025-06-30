from youtool import YouTube

def connectYouTube(apiKey: str) -> YouTube:
    yt = YouTube(api_keys=[apiKey], disable_ipv6=True)
    return yt

def getComments(yt: YouTube, video_id: str):
    try:
        yield from yt.video_comments(video_id)
    except RuntimeError as err:
        if "commentsDisabled" in str(err):
            print(f"Comentários desativados em {video_id} – pulando")
            return
        raise