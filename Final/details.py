from tkinter import *
from PIL import Image, ImageTk


top=Toplevel()
top.title("O shop MART")
top.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
top.configure(background="white")
top.geometry("500x500")

photo=PhotoImage(file="bg.png")
Label(top,image=photo).place(relwidth=1,relheight=1)

label=Label(top,text="Please give your details to go further \n for Payment...",fg="white",bg="dark blue",
            justify=LEFT,font="Constantia 19 bold",padx=200).pack(anchor="w")

Label(top,text="First Name",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=100)
Label(top,text="Last Name",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=140)
Label(top,text="Phone no",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=180)
Label(top,text="Address",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=220)
Label(top,text="e-mail",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=260)
Label(top,text="Altenate phone.no",font="Constantia 15 bold",fg="blue",bg="white").place(x=5,y=300)

fname=StringVar()
lname=StringVar()
ph=IntVar()
add=StringVar()
email=StringVar()
aph=IntVar()

Entry(top,textvariable=fname,width=30,border=3).place(x=250,y=105)
Entry(top,textvariable=lname,width=30,border=3).place(x=250,y=145)
Entry(top,textvariable=ph,width=30,border=3).place(x=250,y=185)
Entry(top,textvariable=add,width=30,border=3).place(x=250,y=225)
Entry(top,textvariable=email,width=30,border=3).place(x=250,y=265)
Entry(top,textvariable=aph,width=30,border=3).place(x=250,y=305)

Button(top,text="Go to payment section",bg="orange",fg="black",font="Constantia 15 bold").place(x=100,y=380)
Button(top,text="Back",font="Constantia 15 bold",command=top.destroy).place(x=180,y=430)


mainloop()