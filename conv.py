from __future__ import unicode_literals
from tkinter import *
from tkinter.filedialog import askdirectory
import youtube_dl
import sys

pesme = []
folder = "C:/Users/Siki/Desktop/py/YtMp3/dwnld/%(title)s.%(ext)s"

def skiniSve():
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': folder,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],}

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(pesme)
            Label(master, text= "Uspelo skidanje %d" %(pesme.__len__), fg="green").grid(row= 4)
    except TypeError:
        print("Sve ok dw :)")
        Label(master, text= "Uspelo skidanje %d item-a" %(len(pesme)), fg="green").grid(row= 4)
    except:
        print(sys.exc_info()[0])
        Label(master, text= "Neuspelo skidanje", fg= "red").grid(row= 4)


def dodajUQ():
    pesme.append(e1.get())

def noviFolder():
    global folder 
    folder = askdirectory() + "/%(title)s.%(ext)s"
    print(folder)





master = Tk()
master.title("Konverter")
master.geometry("500x120")

#lista = Listbox(master, width= 60)


Label(master, text= "YouTube URL: ").grid(row= 0)

e1 = Entry(master, width= 60)

e1.grid(row= 0, column= 1)
Button(master, text= "Dodaj u queue", command= dodajUQ).grid(row= 2, column= 0, sticky= W, pady= 4)
Button(master, text= "Konvertuj i skini", command= skiniSve).grid(row= 2, column= 1, sticky= W, pady= 4)
Button(master, text= "Dwnld dest", command= noviFolder).grid(row= 3, column= 0, sticky= W, pady= 4)
#lista.grid(row=3, column= 0, )

mainloop()