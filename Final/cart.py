from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql


def insert():

    a1=e_r.get()
    b1=e_n.get()
    c1=e_s.get()
    d1=e_m.get()

    conn=mysql.connect(host="localhost",user="root",passwd="ckm111003",database="studentdb",
                       auth_plugin='caching_sha2_password')
    cursor=conn.cursor()
    cursor.execute("insert into Student values( '"+ a1 +"','"+ b1 +"','"+ c1 +"','"+ d1 +"')")
    cursor.execute("commit")

    conn.close

def delete():
    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                         auth_plugin='caching_sha2_password')
    cursor = con.cursor()
    cursor.execute("delete from Student where roll_no= ' " + e_r.get() + " ' ")
    cursor.execute("commit")

    con.close

def show():
    root = Toplevel()
    root.title("O shop MART")
    root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
    root.geometry("500x500")

    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                        auth_plugin='caching_sha2_password')
    cursor = con.cursor()
    cursor.execute(" select * from Student ")
    rows = cursor.fetchall()
    for row in rows:
        ins=str(row[0])+"                           "+str(row[1])+"                         "+row[2]
        Label(root,text=ins).pack(anchor="w")

    con.close()

root=Tk()
root.title("O shop MART")
root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
root.geometry("500x500")

a=Label(root,text="Roll No",font=('bold,10')).place(x=20,y=30)
b=Label(root,text="Name",font=('bold,10')).place(x=20,y=60)
c=Label(root,text="Subject",font=('bold,10')).place(x=20,y=90)
d=Label(root,text="Marks",font=('bold,10')).place(x=20,y=120)

e_r=Entry()
e_r.place(x=150,y=30)
e_n=Entry()
e_n.place(x=150,y=60)
e_s=Entry()
e_s.place(x=150,y=90)
e_m=Entry()
e_m.place(x=150,y=120)

Button(root,text="Insert",font=('bold ',10),command=insert).place(x=20,y=150)
Button(root,text="Delete",font=('bold ',10),command=delete).place(x=90,y=150)
Button(root,text="Show",font=('bold ',10),command=show).place(x=160,y=150)

mainloop()

