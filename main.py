import yt_dlp

def main():
    URLS = ['https://youtu.be/JNIK18PKrqY?si=Ycd1qCjYazf7_anv']

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  
            #'ffmpeg_location': r'C:\Users\User\Desktop\Visual studio\youtube_to_mp3\ffmpeg-8.0.1',  
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

if __name__ == "__main__":
    main()
