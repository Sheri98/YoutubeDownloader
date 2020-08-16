import pytube
import re
from pytube import Playlist
from pytube import YouTube

def PlayListDownload():
    URL = str(input("[*] Enter The Playlist Url:"))
    PATH = str(input("[*] Enter The Path To be Downloaded To For Default Path Simple Enter 1:"))
    Playlist_Url_Obj = Playlist(URL)
    Playlist_Url_Obj._video_regex  = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(f"[*] Number Of Videos In PlayList : {len(Playlist_Url_Obj.video_urls)}")
    number=1
    for video_url in Playlist_Url_Obj.video_urls:
        if PATH == "1":
            obj = YouTube(video_url).streams.first().download()
            print(f"[*] Total Downloaded Videos {number}")
            number+=1
        else:
            obj = YouTube(video_url).streams.first().download(PATH)
            print(f"[*] Total Downloaded Videos {number}")
            number += 1
    number = 1
def YoutubeVideo():
    URL = str(input("[*] Enter The Youtube Video Url:"))
    PATH = str(input("[*] Enter The Path To be Downloaded To For Default Path Simple Enter 1:"))
    Single_Video_Url = YouTube(URL).streams.first()
    print(f"Starting To Download The Video:")
    if PATH == "1":
        Single_Video_Url.download()
        print("Video Has Been Downloaded")
    else:
        Single_Video_Url.download(PATH)
        print("Video Has been Downloaded")
def main():
    print("[*] Youtube Downloader:")
    Function_Call = str(input("[*] Select What Type You Want To Download \n"
          "[*] For Playlist Enter 1 : \n"
          "[*] For SingleVideo Enter 2 : \n"
          "[*] Enter The Number: "))
    if Function_Call == "1":
        PlayListDownload()
    else:
        YoutubeVideo()
if __name__ == '__main__':
    main()


