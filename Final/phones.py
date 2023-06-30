from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql

top=Tk()
top.title("O shop MART")
top.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
top.configure(background="white")
top.geometry("500x550")

def insert(a,b,c,):
    a1=a
    b1=b
    c1=c

    conn=mysql.connect(host="localhost",user="root",passwd="ckm111003",database="studentdb",
                       auth_plugin='caching_sha2_password')
    cursor=conn.cursor()
    cursor.execute("insert into shop values( '"+ str(a1) +"','"+ str(b1) +"','"+ c1 +"')")
    cursor.execute("commit")

    conn.close

def delete():
    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                         auth_plugin='caching_sha2_password')
    cursor = con.cursor()
    cursor.execute("delete from shop where slno= ' " + a + " ' ")
    cursor.execute("commit")

    con.close

def show():

    global en
    root = Toplevel()
    root.title("O shop MART")
    root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
    root.geometry("500x500")

    op = ImageTk.PhotoImage(Image.open("Oneplus.jpg"))
    Label(root, image=op).place(x=450, y=70)

    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                        auth_plugin='caching_sha2_password')
    cursor = con.cursor()
    cursor.execute(" select * from shop ")
    rows = cursor.fetchall()
    for row in rows:
        ins=str(row[0])+"\t"+str(row[1])+"     "+str(row[2])
        Label(root,text=ins).pack(anchor="w")

    con.close()

    total = int(clicked.get()) * int(59999)
    Label(root, text=total, fg="black", bg="white", font="Constantia 14 bold").place(x=100, y=100)

    mainloop()



label=Label(top,text="In Headphones...",fg="white",bg="dark blue",justify=LEFT,padx=200,
            font="Constantia 19 bold").pack(anchor="w")
Label(top,text="""Apple AirPods Pro"""
      ,fg="black",bg="white", padx=200,font="Constantia 14 bold").pack(anchor="w")

op=ImageTk.PhotoImage(Image.open("Oneplus.jpg"))
Label(top,image=op).place(x=10,y=70)

Label(top,text="""Price: ₹ 59,999.00 \n Delivey: Free delivery \n Delivery by: 11-Oct-2020""",
      fg="black",bg="white",font="Constantia 14 bold").place(x=255,y=110)

Button(top,text="View more Images",fg="blue",border=5,font="Constantia 9 bold",command=lambda:insert(2,"One plus",clicked.get())).place(x=35,y=290)
Button(top,text="Buy Now!",bg="orange",fg="black",border=3,width=20,font="Constantia 9 bold").place(x=275,y=201)
Button(top,text="Back",fg="blue",border=3,width=15,font="Constantia 9 bold",command=top.destroy).place(x=260,y=236)
Button(top,text="Cart",bg="orange",fg="black",border=3,width=5,font="Constantia 9 bold",command=show).place(x=380,y=40)

Label(top,text="About this item:",fg="black",bg="white",font="Constantia 19 bold").place(x=30,y=321)

Label(top,text="""
1) 48MP rear camera with 4K video at 30/60 fps.
2) 16MP front camera.
3) 6.78-inch, 120Hz fluid display with 3168x1440 pixels resolution.
4) Memory, Storage & SIM: 12GB RAM | 256GB internal memory 
   | Dual SIM (nano+nano) dual-standby(5G+5G). 
5) Oxygen OS based on Android v10 operating system with 2.86GHz of clock speed with Qualcomm.
6) 4510mAH lithium-ion battery.""",fg="black",bg="white",font="Constantia 12",justif=LEFT).place(x=10,y=350)


clicked=StringVar()
clicked.set(1)
drop=OptionMenu(top,clicked,"1","2","3","4","5","6","7")
drop.place(x=400,y=236)


mainloop()