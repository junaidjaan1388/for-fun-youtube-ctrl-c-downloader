import threading
import time
import youtube_dl
import pyperclip


def watch_clipboard():
    print("I'm watching your clipboard 👀")
    print("If you copy an youtube video link, I'll try to download its audio. ")
    new = pyperclip.paste()
    while True:
        old = new
        while old == new:
            new = pyperclip.paste()
            time.sleep(0.1)
        if "www.youtube.com" in new:
            threading.Thread(target=lambda: dl(new)).start()


def dl(link: str):
    print(f"Downloading {link}... ⌛")
    opts = {
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    }
    youtube_dl.YoutubeDL(opts).download([link])
    print(f"Download of {link} completed ✔")


if __name__ == "__main__":
    watch_clipboard()

