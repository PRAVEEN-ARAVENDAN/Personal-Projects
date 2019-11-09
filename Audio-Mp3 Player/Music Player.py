'''
1) Code for a basic Audio Mp3 player Using Python
2) alt+enter on any function will add the required import statement for that function
'''

import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter.ttk import *

root = Tk() # tkinter function to create a window
root.minsize(300,300)

listofsongs = [] # List of songs from a directory
realnames = []  # List of songs from a directory with full names (Contains full path in the name)

v = StringVar()#initialisation, Part of Tkinter
songlabel = Label(root,textvariable=v,width=35)

index = 0





# Button Operations
def nextsong(event): #"event" takes the left click as argument, event is part of Python itself
    global index # Keep index global
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def updatelabel():
    global index
    global songname
    v.set(realnames[index])


def directorychooser():
    directory = askdirectory()
    os.chdir(directory) # changes current working directory to given path

    for files in os.listdir(directory):
        if files.endswith('.mp3'):

            realdir = os.path.realpath(files) # Gives the whole path to the file
            audio = ID3(realdir) # This mutagen function requires the full path to the file
            realnames.append(audio['TIT2'].text[0]) # TIT2 tag returns title from the metadata (More info is avaiable in Mutagen DOcumentation)

            listofsongs.append(files)
            #print(files)

    #Play Music
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0]) #Plays the first song
    pygame.mixer.music.play()
    #pygame.mixer.music.stop() #Stops the Song

directorychooser()










# VISUAL GUI (USing functions from tkinter package)

label = Label(root,text='My Music Player')
label.pack() # This geometry manager organizes widgets in blocks before placing them in the parent widget.

listbox = Listbox(root) # will contain the list of songs
listbox.pack()

realnames.reverse()# Reversing the list so that its displayed in the right order in the GUI
for items in realnames:
    listbox.insert(0,items) # or use listbox.insert(END,items) instead of reversing the list twice
realnames.reverse() # Reversing again to restore the right order

#Style is created an used on the buttons
style = Style()
style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'green')


nextbutton = Button(root, text='Next Song', style='W.TButton')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song', style='W.TButton')
previousbutton.pack()

stopbutton = Button(root, text='Stop Song', style='W.TButton')
stopbutton.pack()

#Binding Buttons to their functions ,<Button-1> :- Left Click , <Button-2> :- Middle Click, <Button-3> :- Right Click

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()









root.mainloop() # Keeps the GUI Window alive (It runs in an infinite loop) until closed explicitly
