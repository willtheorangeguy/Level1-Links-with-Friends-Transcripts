"""
This script uses yt-dlp to download videos, by year,
from the Level 1 Links with Friends YouTube Channel.
"""

import sys
import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all videos from a YouTube playlist.
    """
    ydl_opts = {
        'format': 'bv+ba',
        'outtmpl': '%(upload_date>%Y)s/%(title)s.%(ext)s',
        'noplaylist': False,
        'ignoreerrors': True,
        'download_archive': 'downloaded.log',
        'remote-components': 'ejs:github',
        'concurrent-fragments': True,
        'no-mtime': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PLcq4cFFv50gtSUtKIRKv7ssIrWgV6nQg0"
    download_playlist(playlist)
    print("Downloaded all videos from The Level 1 Links with Friends podcast.")
