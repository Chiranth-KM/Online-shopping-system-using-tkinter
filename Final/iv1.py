from tkinter import *
from PIL import Image, ImageTk


root=Tk()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.geometry("500x500")

img1=ImageTk.PhotoImage(Image.open("Apple Mac book/am1.jpg"))
img2=ImageTk.PhotoImage(Image.open("Apple Mac book/am2.jpg"))
img3=ImageTk.PhotoImage(Image.open("Apple Mac book/am3.jpg"))
img4=ImageTk.PhotoImage(Image.open("Apple Mac book/am4.jpg"))
img5=ImageTk.PhotoImage(Image.open("Apple Mac book/am5.jpg"))
img6=ImageTk.PhotoImage(Image.open("Apple Mac book/am6.jpg"))


img_list=[img1,img2,img3,img4,img5,img6]
ino=0

l=Label(root,image=img_list[ino])
l.pack()
def forward():
    global ino,l
    l.place_forget()
    ino=ino+1
    if ino<=len(img_list)-1:
        Label(root,image=img_list[ino]).pack()
        Button(root,text=">>>",command=forward).place(x=160,y=100)
        Button(root, text="<<<", command=forward).place(x=100, y=100)
    else:
        root.destroy()

def back():
    global ino,l
    l.place_forget()
    ino=ino-1
    if ino>=0:
        Label(root,image=img_list[ino]).pack()
        Button(root,text=">>>",command=forward).place(x=160,y=100)
        Button(root, text="<<<", command=forward).place(x=100, y=100)
    else:
        screen.destroy()


Button(root,text=">>>",command=forward).place(x=160,y=100)
Button(root,text="<<<",command=back).place(x=100,y=100)

mainloop()