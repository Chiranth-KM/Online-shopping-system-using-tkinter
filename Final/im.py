from tkinter import *
from PIL import Image, ImageTk
import os

root=Tk()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.geometry("500x500")

def resize_image(root,copy,label1):
    new_height=500
    new_width=500
    image=copy.resize((new_height,new_width))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image=photo

def next():
    global n
    global items_list
    n=n+1
    img1 = items_list[n]

    image = Image.open('./Apple Mac book/' + img1)
    copy = image.copy()
    photo = ImageTk.PhotoImage(image)

    label1 = Label(root, image=photo)
    label1.bind('<configure>', resize_image(root, copy, label1))
    label1.pack()

n=0
items_list=os.listdir("Apple Mac book")
img1=items_list[n]

image=Image.open('./Apple Mac book/'+img1)
copy=image.copy()
photo=ImageTk.PhotoImage(image)

label1=Label(root,image=photo)
label1.bind('<configure>',resize_image(root,copy,label1))
label1.pack()

b1=Button(root,text=">>",command=next,width=5,height=10)
b1.place(x=570,y=150)

mainloop()