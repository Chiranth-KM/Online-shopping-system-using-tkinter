from tkinter import *
from PIL import Image, ImageTk


root=Tk()
root.title("O shop MART")
root.iconbitmap('D:\Final\icon.ico')
root.geometry("500x500")

img1=ImageTk.PhotoImage(Image.open("Apple Mac book/am1.jpg"))
img2=ImageTk.PhotoImage(Image.open("Apple Mac book/am2.jpg"))
img3=ImageTk.PhotoImage(Image.open("Apple Mac book/am3.jpg"))
img4=ImageTk.PhotoImage(Image.open("Apple Mac book/am4.jpg"))
img5=ImageTk.PhotoImage(Image.open("Apple Mac book/am5.jpg"))
img6=ImageTk.PhotoImage(Image.open("Apple Mac book/am6.jpg"))


img_list=[img1,img2,img3,img4,img5,img6]
my_label=Label(image=img1)
my_label.place(x=0,y=0)

def forward(ino):
    global my_label
    global forward
    global back

    my_label.place_forget()
    my_label=Label(image=img_list[ino-1])
    bf=Button(root,text=">>",command=lambda:forward(ino+1))
    bb=Button(root,text="<<",command=lambda:back(ino-1))

    if ino==5:
        bf = Button(root, text=">>", state=DISABLED)

    my_label.place(x=0,y=0)
    bb.place(x=100,y=100)
    bf.place(x=170,y=100)

def back(ino):
    global my_label
    global forward
    global back

    my_label.place_forget()
    my_label = Label(image=img_list[ino - 1])
    bf = Button(root, text=">>", command=lambda: forward(ino + 1))
    bb = Button(root, text="<<", command=lambda: back(ino - 1))

    if ino==1:
        bb = Button(root, text="<<", state=DISABLED)

        my_label.place(x=0, y=0)
        bb.place(x=100, y=100)
        bf.place(x=170, y=100)
bb=Button(root,text="<<",command=back,state=DISABLED)
be=Button(root,text="exit",command=root.quit)
bf=Button(root,text=">>",command=lambda:forward(2))

bb.place(x=100, y=100)
be.place(x=0,y=0)
bf.place(x=170, y=100)

mainloop()
