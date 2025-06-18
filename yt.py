from youtool import YouTube

def connectYouTube(apiKey: str) -> YouTube:
    yt = YouTube(api_keys=[apiKey], disable_ipv6=True)
    return yt