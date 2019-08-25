from tkinter import *
from math import floor
from PIL import Image, ImageTk
import os

def mouse_wheel(event):
    global count
    if event.num == 5 or event.delta == -120:
        count -=1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count

count = 0

def update_scrollregion(event):
    photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

def callback(num):
    temp = filenames[num]
    #heres some shit that we will need later
    readConfig = open('/home/holden/.i3/config')
    lines = readConfig.readlines()
    readConfig.close()
    w = open('/home/holden/.i3/config','w')
    w.writelines([item for item in lines[:-1]])
    w.write('exec_always --no-startup-id feh --bg-fill /home/holden/Downloads/wallpapers/'+ temp)
    w.close()
    os.system('i3-msg restart')

imagearray = []
filenames = []
wall_list = os.listdir('/home/holden/Downloads/wallpapers/')
num_walls = len(wall_list)
for filename in os.listdir('/home/holden/Downloads/wallpapers/'):
    filenames.append(filename)


root = Tk()
root.title("please select a wallpaper")
photoFrame = Frame(root,width=1900,height=500,bg="#232629")
photoFrame.grid()
photoFrame.rowconfigure(0,weight=1)
photoFrame.columnconfigure(0,weight=1)
photoCanvas = Canvas(photoFrame,bg="#232629",width=1900,height=1000)
photoCanvas.grid(row=0,column=0,sticky="nsew")
canvasFrame = Frame(photoCanvas,bg="#EBEBEB",width=1900,height=1000)
photoCanvas.create_window(0,0,window=canvasFrame,anchor='nw',width=1850,height=200*floor((num_walls/9))+200)




for file in os.listdir('/home/holden/Downloads/wallpapers/'):
    picture = Image.open(os.path.join('/home/holden/Downloads/wallpapers/',file))
    picture = picture.resize((200,200),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(picture)
    imagearray.append(photo)


buttons = []
count = 0
for j in range(0,num_walls):
    buttons.append(Button(canvasFrame,image=imagearray[j],command=(lambda j=j:callback(j)),height=200,width=200,highlightbackground = '#232629',compound=LEFT,borderwidth=0))

    if j%9 == 0:
        count +=1

    buttons[j].grid(row =count , column = j % 9)

photoScroll = Scrollbar(photoFrame,orient = VERTICAL)
photoScroll.config(command=photoCanvas.yview)
photoScroll.config(bg="#232629")
photoCanvas.config(yscrollcommand=photoScroll.set)
photoScroll.grid(row=0,column=1,sticky="ns")
canvasFrame.bind("<Configure>",update_scrollregion)
root.bind("<Button-4>",mouse_wheel)
root.bind("<Button-5>",mouse_wheel)


root.mainloop()
