import os
import yt_dlp

def download_audio(url, folder_name):
    os.makedirs(folder_name, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg'),  
        'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
        'noplaylist': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    folder = input("Enter folder name: ").strip()
    if url and folder:
        download_audio(url, folder)
