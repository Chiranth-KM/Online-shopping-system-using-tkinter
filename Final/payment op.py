from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql

root=Toplevel()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.configure(background="white")
root.geometry("500x495")

photo=PhotoImage(file="payment.png")
Label(root,image=photo).place(relwidth=1,relheight=1)

con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                        auth_plugin='caching_sha2_password')

cursor = con.cursor()
cursor.execute("""  update shop
                        set final_cost=quantity*total
                        where final_cost="NULL" """)
cursor.execute("select sum(final_cost) from shop")

rows = cursor.fetchall()
for row in rows:
    ins=str(row[0])
    Label(root,text="Amount to pay:"+ins,fg="black",bg="white",font="Constantia 14 italic").place(x=10,y=40)
con.close()

def cards():
    Label(root, text="Name on Card", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=110)
    Label(root, text="Card Number", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=150)
    Label(root, text="Validity", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=190)
    Label(root, text="CVV", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=230)
    Label(root, text="/", fg="blue", bg="white",font="Constantia 14 italic").place(x=299, y=234)

    nc = StringVar()
    cn = StringVar()
    v = StringVar()
    c = StringVar()
    c1=StringVar()

    Entry(root, textvariable=nc, width=30, border=3).place(x=250, y=115)
    Entry(root, textvariable=cn, width=30, border=3).place(x=250, y=155)
    Entry(root, textvariable=v, width=30, border=3).place(x=250, y=195)
    Entry(root, textvariable=c, width=5, border=3).place(x=250, y=235)
    Entry(root, textvariable=c1, width=5, border=3).place(x=325, y=235)

def confirmation():
    response = messagebox.askyesno(title="Confirmation", message="Are you sure you want to book you product??")
    if response==1:
        Label(root,text="hi").place(x=100, y=100)

    elif response==0:
        Label(root,text="hola").place(x=100, y=100)

var=StringVar()
var.set("Radio")

label=Label(root,text="Please select the mode of payment...",fg="white",bg="dark blue",justify=LEFT,padx=200,
            font="Constantia 19 bold").pack(anchor="w")

radio=Radiobutton(root,text="Debit card/ Credit card",padx=14,variable=var,value="1",fg="blue",
                  bg="white",command=cards,font="Constantia 11 italic").place(x=10, y=80)
radio=Radiobutton(root,text="Cash on Delivery",padx=14,variable=var,value="2",fg="blue",bg="white",
                  font="Constantia 11 italic").place(x=10, y=310)


Button(root,text="Submit",padx=24,command=confirmation,bg="yellow",fg="black",font="Constantia 14 italic").place(x=200, y=400)
Button(root,text="Back",padx=26,command=root.quit,font="Constantia 14 italic").place(x=205, y=450)


mainloop()