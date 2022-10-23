from tkinter import *
from tkinter.ttk import *
from pytube import YouTube

# create window
window = Tk()
window.title("Youtube Downloader")
window.geometry('500x200')

# create label
lbl = Label(window, text="Enter Youtube Link")
lbl.grid(column=0, row=0)

# create text box
txt = Entry(window, width=40)
txt.grid(column=1, row=0)

def clicked():
    link = txt.get()
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download(r'C:\Users\14058\Videos\Downloaded')
    lbl.configure(text="Download Complete")

btn = Button(window, text="Download", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()
