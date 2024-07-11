import os
from tkinter import *
from yt_dlp import YoutubeDL

root = Tk()
root.geometry('450x300')
root.title("YouTube Video Downloader")

Label(root, text='Youtube Video Downloader', font='arial 15 bold').pack()
link = StringVar()
filename = StringVar()

Label(root, text='원하는 링크 url 복사', font='arial 13 bold').place(x=160, y=40)
link_enter = Entry(root, width=45, textvariable=link).place(x=50, y=90)

def Download():
    Label(root, text='Downloading', font='arial 13').place(x=180, y=210)
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link.get()])
    Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)

Button(root, text='Download', font='arial 15 bold', padx=2, command=Download).place(x=180, y=150)

root.mainloop()
