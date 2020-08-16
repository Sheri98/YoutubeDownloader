import pytube
import re
from pytube import Playlist
from pytube import YouTube
#def progressmeter(stream, chunk, file_handle, bytes_remaining):
   # print(round((1-bytes_remaining/single_Vide.filesize)*100, 3), '% done...')
def PlayListDownload():
    URL = str(input("Enter The Playlist Url:"))
    PATH = str(input("Enter The Path To be Downloaded To:"))
    Playlist_Url_Obj = Playlist(URL)
    Playlist_Url_Obj._video_regex  = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(f"Number Of Videos In PlayList : {len(Playlist_Url_Obj.video_urls)}")
    for video_url in Playlist_Url_Obj.video_urls:
        obj = YouTube(video_url).streams.first().download(PATH)
        print(f"Downloaded {obj.title} Video")
def YoutubeVideo():
    URL = str(input("Enter The Youtube Video Url:"))
    PATH = str(input("Enter The Path To be Downloaded To:"))
    Single_Video_Url = YouTube(URL).streams.first()
    print(f"Starting To Download The Video:")
    Single_Video_Url.download(PATH)
def main():
    print("Youtube Downloader:")
    Function_Call = str(input("Select What Type You Want To Download \n"
          "For Playlist Enter 1 : \n"
          "For SingleVideo Enter 2 : \n"
          "Enter The Number "))
    if Function_Call == "1":
        PlayListDownload()
    else:
        YoutubeVideo()
if __name__ == '__main__':
    main()


