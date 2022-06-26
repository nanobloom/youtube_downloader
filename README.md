What the program does?

- It's a downloader that lets user download videos from youtube (as the name suggests ^^) using pytube and youtube_dl libraries
- Has a simple user interface built using Tkinter
- User has a choice of downloading video (best available quality .mp4), song (best available quality .mp3) or entire playlist of videos
- Everything is downloaded into "downloads" folder created on first use
- Logging system is also added so that user can keep track on when exactly specific video/song/playlist has been downloaded


How to use it?

Before first use, you need to make sure you're meeting the requirements from requirements.txt. Will try to figure out ways around that like getting PyInstaller to work on Windows without flagging my compiled binaries as security threats.
Using the program is as simple as running the code, waiting for tkinter window to pop up, selecting the type of file/s you want to download, pasting the link and clicking download. Download is completed as soon as the pasted link disappears.
