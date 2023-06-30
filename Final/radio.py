from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.configure(background="white")
root.geometry("500x550")

def order():
    if var.get()=="1":
        Label(root, text="hi").pack()
    elif var.get()=="2":
        Label(root,text="hello").pack()
    elif var.get()=="3":
        Label(root,text="hola").pack()


var=StringVar()
var.set("Radio")

label=Label(root,text="You logged in.....",fg="white",bg="dark blue",justify=LEFT,padx=200,
            font="Constantia 19 bold").pack(anchor="w")
products=Label(root,text="We have following Electronics..",fg="white",bg="dark blue",justify=LEFT,padx=100,
               font="Constantia 19 bold").pack(anchor="w")

radio=Radiobutton(root,text="Headphones",padx=14,variable=var,value="1",fg="blue",bg="white").place(x=290,y=290)
img1=Image.open("headphones.jpg")
photo1=ImageTk.PhotoImage(img1)
a_label=Label(image=photo1)
a_label.place(x=250,y=80)


radio=Radiobutton(root,text="Laptops",padx=14,variable=var,value="2",fg="blue",bg="white").place(x=45,y=270)
img2=Image.open("laptop.jpg")
photo2=ImageTk.PhotoImage(img2)
a_label=Label(image=photo2)
a_label.place(x=12,y=80)

radio=Radiobutton(root,text="Smart Phones",padx=14,variable=var,value="3",fg="blue",bg="white").place(x=75,y=495)
img=Image.open("phone.jpg")
photo=ImageTk.PhotoImage(img)
a_label=Label(image=photo)
a_label.place(x=85,y=315)


Button(root,text="Submit",command=order,padx=24,bg="yellow",fg="black").place(x=320,y=420)



mainloop()

