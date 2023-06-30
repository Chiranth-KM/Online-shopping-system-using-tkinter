from tkinter import *
from PIL import Image, ImageTk
import pickle


root=Tk()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.geometry("500x500")




def write(a,b,c):
    file=open("cart",'wb')
    rec=[a,b,c]
    pickle.dump(rec,file)
    file.close()
def read():
    file = open("cart", 'rb')
    o = pickle.load(file)
    for i in o:
        Label(root,text=i).place(x=3, y=5)
air = ImageTk.PhotoImage(Image.open("Airpods - Copy.jpg"))
Label(root, image=air).place(x=350, y=5)

read()

#Button(root,text="click",command=read).pack()

mainloop()

