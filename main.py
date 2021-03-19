from tkinter import Tk, StringVar, END, Entry, Button, Label, Radiobutton
from pytube import YouTube, Playlist
from youtube_dl import YoutubeDL
from shutil import move

import os
import logging


# Assigning a separate logger and configurating its' handler

log_file = 'Download.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s    %(message)s', datefmt='%H:%M:%S  %d/%m/%Y')

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Assigning a Tkinter's Tk class to a variable to further set the dimensions and title

root = Tk()

root.geometry("320x140")
root.title("Youtube Downloader")


# Assigning class StringVar to use it for accessing and creating variables in the Tcl interpreter

sv = StringVar()


# Preparing dictionary of parameters for FFmpeg postprocessing used to convert downloaded video files into .mp3's for YoutubeDL

parameters = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredquality': '192',
        'preferredcodec': 'mp3',
    }],
}


# Defining Song function for YoutubeDL, E1 is Entry tkinter widget

def Song():
    song = E1.get()
    with YoutubeDL(parameters) as yt:
        info_dict = yt.extract_info(song)
        song_title = info_dict.get('title', None)
        logger.info(f"User downloaded song:  {song_title}")
        for item in os.listdir():
            if item.startswith(song_title):
                filename, ext = os.path.splitext(item) # files are keeping part of url which we are getting rid of at this point
                filename = filename[:-12]
                result = filename + ext
                os.rename(item, result)
                if 'downloads' not in os.listdir():
                    os.mkdir('downloads')
                move(result, f"./downloads/{result}")
    E1.delete(0, END) # Making sure that after downloading the file, our entry widget is cleared so we can insert another link


# Defining Video and Playlist functions to be used by YouTube and Playlist classes imported from pytube
# Note: Playlist function goes by the name of "Playlist_function" to make sure it doesn't interfere with imported Playlist class

def Video():
    if 'downloads' not in os.listdir():
        os.mkdir('downloads')
    video = YouTube(E1.get())
    video_name = f"{video.title}.mp4"
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='.\\downloads')
    logger.info(f"User downloaded video:  {video_name}")
    E1.delete(0, END)

    
def Playlist_function():
    if 'downloads' not in os.listdir():
        os.mkdir('downloads')
    playlist = Playlist(E1.get())
    playlist_title = playlist.title
    logger.info(f"User initialized downloading playlist:  {playlist_title}")

    for video in playlist.videos:
        video_name = f"{video.title}.mp4"
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=f".\\downloads\\{playlist_title}\\")
        logger.info(f"User downloaded video:  {video_name}")
    E1.delete(0, END)


# Creating a button widget which is gonna call a proper function on click and adding it to the window

def click(value):
    Button(root, text='Download', command=value, width=30).place(x=50, y=100)

sv.set(Video)


# Assigning tkinter widgets to variables

L1 = Label(root, text="Choose option, insert link and click the button")
R1 = Radiobutton(root, text="Video", variable=sv, value=Video, command=lambda: click(sv.get()))
R2 = Radiobutton(root, text="Song", variable=sv, value=Song, command=lambda: click(sv.get()))
R3 = Radiobutton(root, text="Playlist", variable=sv, value=Playlist_function, command=lambda: click(sv.get()))
E1 = Entry(root, width=50)
B1 = Button(root, text="Download", command=Video, width=30)


# Setting dimensions for widget placement

L1.place(x=40, y=10)
R1.place(x=10, y=40)
R2.place(x=70, y=40)
R3.place(x=130, y=40)
E1.place(x=10, y=70)
B1.place(x=50, y=100)


# Refreshing the tkinter window by infinite loop

root.mainloop()


'''
Next targets for myself:
- prettify the tkinter UI
- display a message in GUI after downloading
'''