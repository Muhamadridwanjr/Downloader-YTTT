import os
from pytube import YouTube
from TikTokApi import TikTokApi

def download_youtube_video(url, save_path="./downloads"):
    """Download video dari YouTube"""
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        stream.download(save_path)
        print(f"Video berhasil diunduh: {yt.title}")
    except Exception as e:
        print(f"Error saat mengunduh video YouTube: {e}")

def download_tiktok_video(url, save_path="./downloads"):
    """Download video dari TikTok"""
    try:
        api = TikTokApi()
        video_data = api.video(url=url).bytes()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        video_name = os.path.join(save_path, "tiktok_video.mp4")
        with open(video_name, "wb") as f:
            f.write(video_data)
        print("Video TikTok berhasil diunduh.")
    except Exception as e:
        print(f"Error saat mengunduh video TikTok: {e}")

if __name__ == "__main__":
    print("Pilih opsi:")
    print("1. Unduh video YouTube")
    print("2. Unduh video TikTok")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == "1":
        url = input("Masukkan URL YouTube: ")
        download_youtube_video(url)
    elif choice == "2":
        url = input("Masukkan URL TikTok: ")
        download_tiktok_video(url)
    else:
        print("Pilihan tidak valid.")
