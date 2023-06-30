from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql

top=Toplevel()
top.title("O shop MART")
top.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
top.configure(background="white")
top.geometry("500x550")


def items():
    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                        auth_plugin='caching_sha2_password')
    cursor = con.cursor(buffered=True)
    cursor.execute("""  update shop
                                   set final_cost=quantity*total
                                   where final_cost="NULL"
                                   """)
    cursor.execute(" select*from shop ")
    rows = cursor.fetchall()
    for row in rows:
        ins = str(row[1]) + "            " + str(row[2]) + "                 " + str(row[3]) + "             " + str(row[4])
        Label(top, text=ins, fg="black", bg="white", font="Constantia 14 ",justify="left").pack(padx=20)
    con.close()


def money():
    con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                        auth_plugin='caching_sha2_password')

    cursor = con.cursor()
    cursor.execute("""  update shop
                            set final_cost=quantity*total
                            where final_cost="NULL" """)
    cursor.execute("select sum(final_cost) from shop")

    rows = cursor.fetchall()
    for row in rows:
        ins = "₹"+str(row[0])
        Label(top, text=ins, fg="black", bg="white", font="ariel 14 italic").place(x=170,y=225)
    con.close()

def thank():
    label = Label(top, text="Your Bill..", fg="white", bg="dark blue", justify=LEFT, padx=200,
                  font="Constantia 19 bold").pack(anchor="w")
    label = Label(top, text="Your order placed for:",fg="black", bg="white",font="Constantia 19 bold").pack(padx=10)
    insr = str("Product") + "        " + str("Quantity") + "        " + str("Cost") + "                " + str("Final")
    Label(top, text=insr, fg="green", bg="white", font="Constantia 14 bold ",justify="left").pack(padx=20)
    items()
    label = Label(top, text="Total cost :", fg="black", bg="white", font="Constantia 19 bold").place(x=10,y=220)
    money()
    label = Label(top, text="Expected Delivery:11-Oct-2020", fg="black", bg="white",
                  font="Constantia 19 bold").place(x=10,y=280)
    label = Label(top, text="Thank You for Shopping!!", fg="red", bg="white", font="algerian 19 bold").place(x=90,y=360)

    Button(top,text="Go to Home Page",border=3,width=15,bg="orange",fg="black",
           font="Constantia 11 italic",command=top.destroy).place(x=180,y=410)
    Button(top, text="LOG OUT", bg="blue",fg="white", border=3, width=15,
           font="Constantia 11 italic", command=top.destroy).place(x=180,y=450)
mainloop()