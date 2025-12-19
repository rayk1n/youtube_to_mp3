import yt_dlp

def main():
    URLS = ['https://youtu.be/O0Cw1SLdxxE?si=VM-2SK2tbzDDvAu4']

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

if __name__ == "__main__":
    main()
