from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql
from tkinter import messagebox

root=Tk()
root.title("O shop MART")
root.iconbitmap('D:\Final\icon.ico')
root.geometry("500x500")


def login():
    top=Toplevel()
    top.title("O shop MART")
    top.iconbitmap('D:\Final\icon.ico')
    top.configure(background="white")
    top.geometry("500x550")

    def last():

        top = Toplevel()
        top.title("O shop MART")
        top.iconbitmap('D:\Final\icon.ico')
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
                ins = str(row[1]) + "            " + str(row[2]) + "                 " + str(
                    row[3]) + "             " + str(row[4])
                Label(top, text=ins, fg="black", bg="white", font="Constantia 14 ", justify="left").pack(padx=20)
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
                ins = "₹" + str(row[0])
                Label(top, text=ins, fg="black", bg="white", font="ariel 14 italic").place(x=170, y=225)
            con.close()

        def thank():
            label = Label(top, text="Your Bill..", fg="white", bg="dark blue", justify=LEFT, padx=200,
                          font="Constantia 19 bold").pack(anchor="w")
            label = Label(top, text="Your order placed for:", fg="black", bg="white", font="Constantia 19 bold").pack(
                padx=10)
            insr = str("Product") + "        " + str("Quantity") + "        " + str("Cost") + "                " + str(
                "Final")
            Label(top, text=insr, fg="green", bg="white", font="Constantia 14 bold ", justify="left").pack(padx=20)
            items()
            label = Label(top, text="Total cost :", fg="black", bg="white", font="Constantia 19 bold").place(x=10,
                                                                                                             y=220)
            money()
            label = Label(top, text="Expected Delivery:11-Oct-2020", fg="black", bg="white",
                          font="Constantia 19 bold").place(x=10, y=280)
            label = Label(top, text="Thank You for Shopping!!", fg="red", bg="white", font="algerian 19 bold").place(
                x=90, y=360)

        thank()

        mainloop()

    def pay():

        root = Toplevel()
        root.title("O shop MART")
        root.iconbitmap('D:\Final\icon.ico')
        root.configure(background="white")
        root.geometry("500x495")

        photo = PhotoImage(file="payment.png")
        Label(root, image=photo).place(relwidth=1, relheight=1)

        con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                            auth_plugin='caching_sha2_password')

        cursor = con.cursor()
        cursor.execute("""  update shop
                                set final_cost=quantity*total
                                where final_cost="NULL" """)
        cursor.execute("select sum(final_cost) from shop")

        rows = cursor.fetchall()
        for row in rows:
            ins =  "₹"+str(row[0])
            Label(root, text="Amount to pay:" "\t" + ins, fg="black", bg="white", font="ariel 14 italic").place(x=10,
                                                                                                                y=40)
        con.close()

        def cards():
            Label(root, text="Name on Card", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=110)
            Label(root, text="Card Number", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=150)
            Label(root, text="CVV", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=190)
            Label(root, text="Validity", font="Constantia 11 italic", fg="blue", bg="white").place(x=5, y=230)
            Label(root, text="/", fg="blue", bg="white", font="Constantia 14 italic").place(x=299, y=234)

            nc = StringVar()
            cn = StringVar()
            v = StringVar()
            c = StringVar()
            c1 = StringVar()

            Entry(root, textvariable=nc, width=30, border=3,fg="green").place(x=250, y=115)
            Entry(root, textvariable=cn, width=30, border=3,fg="green").place(x=250, y=155)
            Entry(root, textvariable=v, width=5, border=3,fg="green").place(x=250, y=195)
            Entry(root, textvariable=c, width=5, border=3,fg="green").place(x=250, y=235)
            Entry(root, textvariable=c1, width=5, border=3,fg="green").place(x=325, y=235)




        var = StringVar()
        var.set("Radio")

        label = Label(root, text="Please select the mode of payment...", fg="white", bg="dark blue", justify=LEFT,
                      padx=200,
                      font="Constantia 19 bold").pack(anchor="w")

        radio = Radiobutton(root, text="Debit card/ Credit card", padx=14, variable=var, value="1", fg="blue",
                            bg="white", command=cards, font="Constantia 11 italic").place(x=10, y=80)
        radio = Radiobutton(root, text="Cash on Delivery", padx=14, variable=var, value="2", fg="blue", bg="white",
                            font="Constantia 11 italic").place(x=10, y=310)

        Button(root, text="Submit", padx=24, command=last, bg="yellow", fg="black",
               font="Constantia 14 italic").place(x=200, y=400)
        Button(root, text="Back", padx=26, command=root.quit, font="Constantia 14 italic").place(x=205, y=450)

        mainloop()

    def det():
        top = Toplevel()
        top.title("O shop MART")
        top.iconbitmap('D:\Final\icon.ico')
        top.configure(background="white")
        top.geometry("500x500")

        photo = PhotoImage(file="bg.png")
        Label(top, image=photo).place(relwidth=1, relheight=1)

        label = Label(top, text="Please give your details to go further \n for Payment...", fg="white", bg="dark blue",
                      justify=LEFT, font="Constantia 19 bold", padx=200).pack(anchor="w")

        Label(top, text="First Name", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=100)
        Label(top, text="Last Name", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=140)
        Label(top, text="Phone no", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=180)
        Label(top, text="Address", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=220)
        Label(top, text="e-mail", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=260)
        Label(top, text="Altenate phone.no", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=300)

        fname = StringVar()
        lname = StringVar()
        ph = IntVar()
        add = StringVar()
        email = StringVar()
        aph = IntVar()

        Entry(top, textvariable=fname, width=30, border=3,fg="red").place(x=250, y=105)
        Entry(top, textvariable=lname, width=30, border=3,fg="red").place(x=250, y=145)
        Entry(top, textvariable=ph, width=30, border=3,fg="red").place(x=250, y=185)
        Entry(top, textvariable=add, width=30, border=3,fg="red").place(x=250, y=225)
        Entry(top, textvariable=email, width=30, border=3,fg="red").place(x=250, y=265)
        Entry(top, textvariable=aph, width=30, border=3,fg="red").place(x=250, y=305)

        """def confirmation():
            response = messagebox.askyesno(title="Confirmation", message="Are you sure you want to book you product??")
            if response == 1:
                pay()
                       """
        Button(top, text="Go to payment section", bg="orange", fg="black", font="Constantia 15 italic",
               command=pay).place(x=100,y=380)

        Button(top, text="Back", font="Constantia 15 bold", command=top.destroy).place(x=180, y=430)

        mainloop()


    def insert(a, b, c, d):
        a1 = a
        b1 = b
        c1 = c
        d1 = d
        e1 = "NULL"

        conn = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                             auth_plugin='caching_sha2_password')
        cursor = conn.cursor()
        cursor.execute(
            "insert into shop values( '" + str(a1) + "','" + str(b1) + "','" + str(c1) + "','" + str(d1) + "','" + str(
                e1) + "')")
        cursor.execute("commit")

        conn.close

    def show():
        global infor
        root = Toplevel()
        root.title("O shop MART")
        root.iconbitmap('D:\Final\icon.ico')
        root.geometry("500x500")
        root.configure(background="white")

        Label(root, text="Review your Cart", fg="white", bg="dark blue",
              justify=LEFT, font="Constantia 19 bold", padx=200).pack(anchor="w")
        ist = str("P_no") + "          " +str("Product") + "        " + str("Quantity") + "        " + str("Cost") + "                " + str(
            "Final")
        Label(root, text=ist, fg="green", bg="white", font="Constantia 13 bold ", justify="left").pack(padx=0)

        con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                            auth_plugin='caching_sha2_password')
        cursor = con.cursor()
        cursor.execute("""  update shop
                            set final_cost=quantity*total
                            where final_cost="NULL"
                            """)
        cursor.execute(" select*from shop ")
        rows = cursor.fetchall()
        for row in rows:
            insr = str(row[0]) + "             " +str(row[1]) + "            " + str(row[2]) + "                   " + str(
                row[3]) + "               " + str(row[4])
            Label(root, text=insr, fg="black", bg="white", font="Constantia 11 bold ", justify="left").pack(padx=20)
        con.close()

        def delete(a):
            con = mysql.connect(host="localhost", user="root", passwd="ckm111003", database="studentdb",
                                auth_plugin='caching_sha2_password')
            cursor = con.cursor()
            cursor.execute("delete from shop where slno= ' " + a + " ' ")
            cursor.execute("commit")
            con.close

            root.destroy()

        Label(root, text="""Select P_no\n to be deleted""", fg="black", bg="white",
              font="Constantia 11 bold").place(x=10, y=350)

        click1 = StringVar()
        click1.set(1)
        drop1 = OptionMenu(root, click1, "1", "2", "3")
        drop1.place(x=200, y=350)

        Button(root, text="Delete!", bg="orange", fg="black", border=3, width=20,
               font="Constantia 9 italic", command=lambda: delete(click1.get())).place(x=300, y=350)

        Button(root,text="CHECKOUT",border=3,bg="green",fg="white",width=20,font="Constantia 9 italic",
               command=det).place(x=300, y=450)
        Button(root, text="Back", border=3, width=5, font="Constantia 9 italic",
               command=root.destroy).place(x=200, y=450)

        mainloop()



    def details():

        top = Toplevel()
        top.title("O shop MART")
        top.iconbitmap('D:\Final\icon.ico')
        top.configure(background="white")
        top.geometry("500x500")

        photo = PhotoImage(file="bg.png")
        Label(top, image=photo).place(relwidth=1, relheight=1)

        label = Label(top, text="Please give your details to go further \n for Payment...", fg="white", bg="dark blue",
                      justify=LEFT, font="Constantia 19 bold", padx=200).pack(anchor="w")

        Label(top, text="First Name", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=100)
        Label(top, text="Last Name", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=140)
        Label(top, text="Phone no", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=180)
        Label(top, text="Address", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=220)
        Label(top, text="e-mail", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=260)
        Label(top, text="Altenate phone.no", font="Constantia 15 bold", fg="blue", bg="white").place(x=5, y=300)

        fname = StringVar()
        lname = StringVar()
        ph = IntVar()
        add = StringVar()
        email = StringVar()
        aph = IntVar()

        Entry(top, textvariable=fname, width=30, border=3).place(x=250, y=105)
        Entry(top, textvariable=lname, width=30, border=3).place(x=250, y=145)
        Entry(top, textvariable=ph, width=30, border=3).place(x=250, y=185)
        Entry(top, textvariable=add, width=30, border=3).place(x=250, y=225)
        Entry(top, textvariable=email, width=30, border=3).place(x=250, y=265)
        Entry(top, textvariable=aph, width=30, border=3).place(x=250, y=305)

        Button(top, text="Go to payment section", bg="orange", fg="black", font="Constantia 9 italic").place(x=100,
                                                                                                            y=380)
        Button(top, text="Back", font="Constantia 9 italic", command=top.destroy).place(x=180, y=430)

        mainloop()


    def order():

        if var.get() == "1":
            top = Toplevel()
            top.title("O shop MART")
            top.iconbitmap('D:\Final\icon.ico')
            top.configure(background="white")
            top.geometry("500x550")

            clicked = StringVar()
            clicked.set(1)
            drop = OptionMenu(top, clicked, "1", "2", "3", "4", "5", "6", "7")
            drop.place(x=400, y=236)


            label = Label(top, text="In Laptops...", fg="white", bg="dark blue", justify=LEFT, padx=200,
                          font="Constantia 19 bold").pack(anchor="w")
            Label(top, text="""Apple MacBook Pro (16-inch, 16GB RAM, 512GB Storage
            2.6GHz, 9th Gen Intel Core i7)""", fg="black", bg="white", padx=200, font="Constantia 14 bold").pack(
                anchor="w")

            apple = ImageTk.PhotoImage(Image.open("Mac.jpg"))
            Label(top, image=apple).pack(anchor="w")

            Label(top, text="""Price: ₹ 1,99,900.00 \n Delivey: Free delivery \n Delivery by: 11-Oct-2020""",
                  fg="black", bg="white", font="Constantia 14 bold").place(x=255, y=110)

            Button(top, text="Add to Cart", fg="blue",bg="orange", border=3, font="Constantia 9 italic",
                   command=lambda: insert(2, "Macbook", clicked.get(),199900)).place(x=320, y=270)
            Button(top, text="Buy Now!", bg="orange", fg="black", border=3, width=20,command=det,
                   font="Constantia 9 italic").place(x=275, y=201)

            Button(top, text="Back", fg="blue", border=3, width=15, font="Constantia 9 italic",
                   command=top.destroy).place(x=260, y=236)
            Button(top, text="Cart", bg="orange", fg="black", border=3, width=5, font="Constantia 9 italic",
                   command=show).place(x=420, y=80)


            Label(top, text="About this item:", fg="black", bg="white", font="Constantia 19 bold").place(x=30, y=300)

            Label(top, text="""
            1) Stunning 16-inch Retina display with true tone Technology.
            2) Ninth-Gen 6-Core Intel Core i7 processor.
            3) Touch Bar & Touch ID. 
            4) Ultafast SSD. 
            5) Intel UHD Graphics.
            6) Upto 11hrs Battery life.""",
                  fg="black", bg="white", justify= LEFT,font="Constantia 12 italic").place(x=0, y=350)


            mainloop()


        elif var.get() == "2":
            top = Toplevel()
            top.title("O shop MART")
            top.iconbitmap('D:\Final\icon.ico')
            top.configure(background="white")
            top.geometry("500x550")

            clicked = StringVar()
            clicked.set(1)
            drop = OptionMenu(top, clicked, "1", "2", "3", "4", "5", "6", "7")
            drop.place(x=400, y=236)

            label = Label(top, text="In Headphones...", fg="white", bg="dark blue", justify=LEFT, padx=200,
                          font="Constantia 19 bold").pack(anchor="w")
            Label(top, text="Apple AirPods Pro", fg="black", bg="white", padx=200, font="Constantia 14 bold").pack(
                anchor="w")

            air = ImageTk.PhotoImage(Image.open("Airpods.jpg"))
            Label(top, image=air).place(x=15, y=75)

            Label(top, text="""Price: ₹ 20,999.00 \n Delivey: Free delivery \n Delivery by: 11-Oct-2020""",
                  fg="black", bg="white", font="Constantia 14 bold").place(x=255, y=110)

            Button(top, text="Add to Cart", fg="blue",bg="orange", border=5, font="Constantia 9 italic",
                   command=lambda: insert(1, "Airpods", clicked.get(),20999)).place(x=320, y=270)
            Button(top, text="Buy Now!", bg="orange", fg="black", border=3, width=20, command=det,
                   font="Constantia 9 italic").place(x=275, y=201)

            Button(top, text="Back", fg="blue", border=3, width=15, font="Constantia 9 italic",
                   command=top.destroy).place(x=260, y=236)
            Button(top, text="Cart", bg="orange", fg="black", border=3, width=5, font="Constantia 9 italic",
                   command=show).place(x=380, y=40)



            Label(top, text="About this item:", fg="black", bg="white", font="Constantia 19 bold").place(x=30, y=300)

            Label(top, text="""
            1) Active noise cancellation for immersive sound.
            2) Three sizes of soft,tapered silicone tips 
               for a customisable fit.
            3) Sweat and water resistant. 
            4) Easy setup for all your Apple devices. 
            5) Quick access to Siri by saying “Hey Siri”.
            6) The wireless charging case delivers more
               than 24 hours of battery life.""",
                  fg="black", bg="white", font="Constantia 12 italic", justify=LEFT).place(x=10, y=350)

            mainloop()


        else:
            top = Toplevel()
            top.title("O shop MART")
            top.iconbitmap('D:\Final\icon.ico')
            top.configure(background="white")
            top.geometry("500x550")

            label = Label(top, text="In Smart Phones...", fg="white", bg="dark blue", justify=LEFT, padx=200,
                          font="Constantia 19 bold").pack(anchor="w")
            Label(top, text="""OnePlus 8 Pro (Glacial Green 12GB RAM+256GB Storage)"""
                  , fg="black", bg="white", padx=200, font="Constantia 13 bold").pack(anchor="w")

            op = ImageTk.PhotoImage(Image.open("Oneplus.jpg"))
            Label(top, image=op).place(x=10, y=70)

            Label(top, text="""Price: ₹ 59,999.00 \n Delivey: Free delivery \n Delivery by: 11-Oct-2020""",
                  fg="black", bg="white", font="Constantia 14 bold").place(x=255, y=110)

            Button(top, text="Add to Cart", fg="blue", bg="orange",border=5, font="Constantia 9 italic",
                   command=lambda: insert(3, "OnePlus", clicked.get(),59999)).place(x=320, y=270)
            Button(top, text="Buy Now!", bg="orange", fg="black", border=3, width=20,command=det,
                   font="Constantia 9 italic").place(x=275, y=201)

            Button(top, text="Back", fg="blue", border=3, width=15, font="Constantia 9 italic",
                   command=top.destroy).place(x=260, y=236)
            Button(top, text="Cart", bg="orange", fg="black", border=3, width=5, font="Constantia 9 italic",
                   command=show).place(x=380, y=70)

            clicked = StringVar()
            clicked.set(1)
            drop = OptionMenu(top, clicked, "1", "2", "3", "4", "5", "6", "7")
            drop.place(x=400, y=236)

            Label(top, text="About this item:", fg="black", bg="white", font="Constantia 19 bold").place(x=30, y=321)

            Label(top, text="""
            1) 48MP rear camera with 4K video at 30/60 fps.
            2) 16MP front camera.
            3) 6.7 inch,120Hz fluid display with 3168x1440 pixels resolution.
            4) Memory, Storage & SIM: 12GB RAM; 256GB internal memory 
               Dual SIM (nano+nano) dual-standby(5G+5G). 
            5) Oxygen OS based on Android v10 operating system 
               with 2.86GHz of clock speed with Qualcomm.
            6) 4510mAH lithium-ion battery.""", fg="black", bg="white", font="Constantia 11 italic",
                  justif=LEFT).place(x=5, y=350)

            mainloop()




    var = StringVar()
    var.set("Radio")


    label = Label(top, text="You logged in.....", fg="white", bg="dark blue", justify=LEFT, padx=200,
                  font="Constantia 19 bold").pack(anchor="w")
    products = Label(top, text="We have following Electronics..", fg="white", bg="dark blue", justify=LEFT, padx=100,
                     font="Constantia 19 bold").pack(anchor="w")

    radio = Radiobutton(top, text="Laptops", padx=14,font="Constantia 11 italic",
                        variable=var, value="1", fg="blue", bg="white").place(x=290,y=290)

    img_1 = ImageTk.PhotoImage(Image.open("laptop.jpg"))
    Label(top,image=img_1).place(x=250, y=100)

    radio = Radiobutton(top, text="Headphones", padx=14, variable=var,
                        font="Constantia 11 italic", value="2", fg="blue", bg="white").place(x=45,y=290)


    img_2 = ImageTk.PhotoImage(Image.open("headphones.jpg"))
    Label(top,image=img_2).place(x=12, y=80)

    radio = Radiobutton(top, text="Smart Phones", padx=14, variable=var,font="Constantia 11 italic",
                        value="3", fg="blue", bg="white").place(x=75,y=495)

    img_3 = ImageTk.PhotoImage(Image.open("phone.jpg"))
    Label(top,image=img_3).place(x=85, y=315)

    Button(top, text="Submit", command=order, padx=24, bg="yellow",font="Constantia 11 italic",
           fg="black").place(x=320, y=420)

    Button(top, text="Cart", bg="orange", fg="black", border=3, width=5, font="Constantia 9 italic",
           command=show).place(x=450, y=40)


    mainloop()



photo=PhotoImage(file="bg.png")
Label(root,image=photo).place(relwidth=1,relheight=1)

my_label = Label(root, text="""Welcome to O Shop MART.
Please enter your username and password....""",fg="white",bg="dark blue", padx=35,
                     font="Constantia 15 bold italic")
my_label.pack()

Label(root, text="Username", font="Constantia 15 italic", fg="green").place(x=5, y=150)
Label(root,text="Password",font="Constantia 15 italic", fg="green",bg="light grey").place(x=5, y=230)

e=Entry(root,width=30,borderwidth=3,fg="blue").place(x=170, y=150)
e1=Entry(root,width=30,borderwidth=3,fg="blue").place(x=170, y=250)


button=Button(root,text="Login",bg="yellow",font="Constantia 11 italic",padx=50,command=login)
button.place(x=185,y=350)
Button(root,text="Close App",font="Constantia 11 italic",command=root.destroy).place(x=220,y=400)
mainloop()