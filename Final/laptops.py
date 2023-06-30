from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql

top=Tk()
top.title("O shop MART")
top.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
top.configure(background="white")
top.geometry("500x550")

def insert(a,b,c,d):
    a1=a
    b1=b
    c1=c
    d1=d
    e1="NULL"

    conn=mysql.connect(host="localhost",user="root",passwd="ckm111003",database="studentdb",
                       auth_plugin='caching_sha2_password')
    cursor=conn.cursor()
    cursor.execute("insert into shop values( '"+ str(a1) +"','"+ str(b1) +"','"+ str(c1) +"','"+ str(d1) +"','"+ str(e1) +"')")
    cursor.execute("commit")

    conn.close


def show():
    root = Toplevel()
    root.title("O shop MART")
    root.iconbitmap('C:/Users/Chiranth/Desktop/project shop/icon.ico')
    root.geometry("500x500")
    root.configure(background="white")

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
        ins=str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])
        Label(root,text=ins,fg="black",bg="white", padx=50,font="Constantia 14 bold").pack(anchor="w")

    con.close()

    def delete(a):
        con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                             auth_plugin='caching_sha2_password')
        cursor = con.cursor()
        cursor.execute("delete from shop where slno= ' " + a + " ' ")
        cursor.execute("commit")
        con.close

        root.destroy()


    Label(root, text="""Enter the product no\n to be deleted""", fg="black", bg="white",
                    font="Constantia 11 bold").place(x=0, y=350)

    k = StringVar()
    Entry(root, textvariable=k, width=10, border=3).place(x=200, y=350)

    Button(root, text="Delete!", bg="orange", fg="black", border=3, width=20,
           font="Constantia 9 bold",command=lambda:delete(k.get())).place(x=300,y=350)

    mainloop()






label=Label(top,text="In Headphones...",fg="white",bg="dark blue",justify=LEFT,padx=200,
            font="Constantia 19 bold").pack(anchor="w")
Label(top,text="Apple AirPods Pro",fg="black",bg="white", padx=200,font="Constantia 14 bold").pack(anchor="w")

air=ImageTk.PhotoImage(Image.open("Airpods.jpg"))
Label(top,image=air).place(x=15,y=75)

Label(top,text="""Price: ₹ 20,999.00 \n Delivey: Free delivery \n Delivery by: 11-Oct-2020""",
      fg="black",bg="white",font="Constantia 14 bold").place(x=255,y=110)



Button(top,text="add to cart",fg="blue",border=5,font="Constantia 9 bold",
         command=lambda:insert(1,"Airpods",clicked.get(),199999)).place(x=70,y=270)
Button(top,text="Buy Now!",bg="orange",fg="black",border=3,width=20,font="Constantia 9 bold").place(x=275,y=201)
Button(top,text="Back",fg="blue",border=3,width=15,font="Constantia 9 bold",command=top.destroy).place(x=260,y=236)
Button(top,text="Cart",bg="orange",fg="black",border=3,width=5,font="Constantia 9 bold",command=show).place(x=380,y=40)

clicked=StringVar()
clicked.set(1)
drop=OptionMenu(top,clicked,"1","2","3","4","5","6","7")
drop.place(x=400,y=236)

Label(top,text="About this item:",fg="black",bg="white",font="Constantia 19 bold").place(x=30,y=300)
q=Label(top,text="quantity",fg="black",bg="white",font="Constantia 19 bold")
q.place(x=10,y=500)


Label(top,text="""
1) Active noise cancellation for immersive sound.
2) Three sizes of soft,tapered silicone tips for a customisable fit.
3) Sweat and water resistant. 
4) Easy setup for all your Apple devices. 
5) Quick access to Siri by saying “Hey Siri”.
6) The wireless charging case delivers more
   than 24 hours of battery life.""",
fg="black",bg="white",font="Constantia 12",justify=LEFT).place(x=10,y=350)

mainloop()

#select slno,P_name,quantity,(quantity*total)as final from shop
#air = ImageTk.PhotoImage(Image.open("Oneplus - Copy.jpg"))
    #Label(root, image=air).pack(anchor="w")