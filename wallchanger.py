'''
This script uses tkinter to make a gui to change wallpapers for those using
i3wm. It takes two arguments, the first one is the path to your i3 config.
The second is the path to the folder where you store your wallpapers.
You're going to make sure you are using feh to set your wallpapers beforehand. 
For this to work you are going to need to installtkinter, feh, i3, and PIL/pillow
'''

from tkinter import Tk, Frame, Canvas, Scrollbar, Button, LEFT, VERTICAL 
from math import floor
from PIL import Image, ImageTk
import os, sys

def update_scrollregion(event): #provide scrolling
    photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

# make sure 2 arguments are included
while True:
    try:
        i3_config = sys.argv[1]
        wall_folder = sys.argv[2]
        break
    except IndexError:
        print("Must include 2 arguments: i3 config location and wallpaper folder")
        exit()
        break


def callback(num):     #function that changes i3 config
    temp = filenames[num]  #save filename of chosen wallpaper
    readConfig = open(i3_config)
    lines = readConfig.readlines()
    for i in range(0,len(lines)):
        if 'feh' in lines[i] and lines[i][0] != '#':
            lines[i] = 'exec_always --no-startup-id feh --bg-scale ' + wall_folder + temp
    config = open(i3_config,'w') #opens i3 config to write
    config.writelines([item for item in lines])
    config.close()  #save i3 config
    os.system('i3-msg restart') #restart i3

imagearray = [] # initialize array of images
filenames = []  # initialize array of file names
wall_list = os.listdir(wall_folder)
num_walls = len(wall_list)
for filename in os.listdir(wall_folder):
    filenames.append(filename)

root = Tk()
root.title("Please select a wallpaper")
photoFrame = Frame(root, width=1900, height=500, bg="#232629")
photoFrame.grid()
photoFrame.rowconfigure(0, weight=1)
photoFrame.columnconfigure(0, weight=1)
photoCanvas = Canvas(photoFrame, bg="#232629", width=1900, height=1000)
photoCanvas.grid(row=0, column=0, sticky="nsew")
canvasFrame = Frame(photoCanvas, bg="#EBEBEB", width=1900, height = 1000)
photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw', width=1850, height=200*floor((num_walls/9))+300)

# create images out of the wallpapers so they can be used on buttons
# this part is slow which is why the script takes some time to start
# not sure how to make it faster
for file in os.listdir(wall_folder):
    picture = Image.open(os.path.join(wall_folder,file))
    picture = picture.resize((200, 200), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(picture)
    imagearray.append(photo)

# create grid of bttton with pictures from wallpaper folder
# when clicked will call callback() function
buttons = []
count = 0
for j in range(0, num_walls):
    buttons.append(Button(canvasFrame, image=imagearray[j],command=(lambda j=j:callback(j)), height=200, width=200, highlightbackground = '#232629', compound=LEFT, borderwidth=0))

    if j%9 == 0:
        count +=1

    buttons[j].grid(row =count , column = j % 9)


photoScroll = Scrollbar(photoFrame, orient=VERTICAL)
photoScroll.config(command=photoCanvas.yview)
photoScroll.config(bg = '#232629')
photoCanvas.config(yscrollcommand=photoScroll.set)
photoScroll.grid(row=0, column=1, sticky="ns")
canvasFrame.bind("<Configure>", update_scrollregion)

root.mainloop()
