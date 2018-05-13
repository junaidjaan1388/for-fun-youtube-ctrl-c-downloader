# youtube-ctrl-c-downloader
Download multiple audio from youtube using ctrl+c. A efficient application of [youtube-dl ](https://github.com/rg3/youtube-dl).


# Description

Run the script

```
python3 main.py
```

When you copy a link to youtube video (ctrl+c), the program will automatically start the download of this video and save the mp3 file on the program directory.


Copy multiple video links. The program will download up to 4 videos at the same time. Any further link will be stored and will be downloaded as soon as a thread become avaliable. This maximum can be raised modifying the MAX_YOUTUBE_DL_THREADS on main.py




