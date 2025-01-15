import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
import pymysql

def passenger():
    master = Tk()
    master.geometry("600x600")
    master.title("Passengers details")



    textName = StringVar()
    textDob = StringVar()
    textPassnum = StringVar()
    textAdh = StringVar()
    textNat = StringVar()

    Label(master, text="Passenger-Name : ",font=("times new roman", 16, "bold")).grid(row=0, pady=5)
    Label(master, text="Date Of Birth : ",font=("times new roman", 16, "bold")).grid(row=1, pady=5)
    Label(master, text="Pass Number : ",font=("times new roman", 16, "bold")).grid(row=2, pady=5)
    Label(master, text="Passenger Aadhar : ",font=("times new roman", 16, "bold")).grid(row=3, pady=5)
    Label(master, text="Nationality : ",font=("times new roman", 16, "bold")).grid(row=4, pady=5)

    Message(master, text="NOTE : Enter the Correct details of the Passengers",
            font=("times new roman", 15, "bold"), fg='blue', width=400).grid(row=21)

    name = Entry(master, text=textName)
    dob = Entry(master, text=textDob)
    passnum = Entry(master, text=textPassnum)
    aadhar = Entry(master, text=textAdh)
    nationality = Entry(master, text=textNat)

    def done():
        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(passnum.get())
        texte = "{}".format(aadhar.get())
        textf = "{}".format(nationality.get())

        print(texta)

        dataa = (texta, textb, textc, texte, textf)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation', autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Passenger VALUES""" + str(dataa))
        db.commit()
        cursor.execute("""SELECT * FROM Passenger;""")
        print(cursor.fetchall())

        db.close()

    def deletePassenger():
        deletePass = Tk()
        deletePass.geometry("600x220")
        deletePass.title("Delete Passenger")

        deletePassInput = StringVar()

        Label(deletePass, text="Pass number : ",font=("times new roman", 16, "bold")).grid(row=0, pady=5)

        Label(deletePass, text="NOTE : Enter the valid pass number to delete ",
              font=("times new roman", 14, "bold"), fg='blue').grid(row=2)

        passDelete = Entry(deletePass, text=deletePassInput)
        passDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(passDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation',
                                 autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''
            cursor.execute("""DELETE FROM Passenger WHERE passnum=""" + str(dataa))
            cursor.execute("""SELECT * FROM passenger;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deletePass, text="Done", command=delete, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=300)

    Buttong = Button(master, text="Delete Passenger", command=deletePassenger, bg="red", fg="white",font=("arial black", 15, "bold")).place(x=20, y=380)

    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)
    passnum.grid(row=2, column=1)
    aadhar.grid(row=3, column=1)
    nationality.grid(row=4, column=1)


def ticket():
    master = Tk()
    master.geometry("600x400")
    master.title("Tickets")


    textTicketNum = StringVar()
    textSeatNum = StringVar()
    textSfrom = StringVar()
    textTo = StringVar()

    Label(master, text="Ticket Number : ",font=("times new roman", 16, "bold")).grid(row=0, pady=5)
    Label(master, text="Seat Number : ",font=("times new roman", 16, "bold")).grid(row=1, pady=5)
    Label(master, text="From : ",font=("times new roman", 16, "bold")).grid(row=2, pady=5)
    Label(master, text="To : ",font=("times new roman", 16, "bold")).grid(row=3, pady=5)

    Label(master, text="NOTE : Enter the details to Book the tickets ", font=("times new roman", 15, "bold"), fg='blue').grid(
        row=16)

    # Change seat number

    ticketNum = Entry(master, text=textTicketNum)
    seatNum = Entry(master, text=textSeatNum)
    sfrom = Entry(master, text=textSfrom)
    to = Entry(master, text=textTo)

    def done():
        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())
        textc = "{}".format(sfrom.get())
        textd = "{}".format(to.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)

        db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation', autocommit=True)
        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Ticket VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Ticket;""")

        print(cursor.fetchall())

        db.close()

    def deleteTicket():
        deleteTick = Tk()
        deleteTick.geometry("600x300")
        deleteTick.title("Delete Tickets")

        deleteTickInput = StringVar()

        Label(deleteTick, text="Ticket Number: ",font=("times new roman", 16, "bold")).grid(row=0)

        Label(deleteTick, text="NOTE : Enter the valid Ticket number that to be deleted",
              font=("times new roman", 12, "bold"), fg='blue').grid(row=4)

        ticketDelete = Entry(deleteTick, text=deleteTickInput)

        ticketDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation',
                                 autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Ticket WHERE ticketNum=""" + str(dataa));
            cursor.execute("""SELECT * FROM Ticket;""")

            print(cursor.fetchall())

            db.close()

        Buttonf = Button(deleteTick, text="Done", command=delete, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=150)


    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=220)
    Buttong = Button(master, text="Delete Ticket", command=deleteTicket, bg="red", fg="white",font=("arial black", 15, "bold")).place(x=20, y=290)

    ticketNum.grid(row=0, column=1)
    seatNum.grid(row=1, column=1, pady=5)
    sfrom.grid(row=2, column=1)
    to.grid(row=3, column=1, pady=5)


def flight():
    master = Tk()
    master.geometry("700x500")
    master.title("Flights")

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighname = StringVar()
    textArrival = StringVar()
    textDeparture = StringVar()
    textDuration = StringVar()
    textCost = StringVar()

    Label(master, text="Flight ID : ",font=("times new roman", 16, "bold")).grid(row=0)
    Label(master, text="Flight Terminal : ",font=("times new roman", 16, "bold")).grid(row=1, pady=5)
    Label(master, text="Flight Name : ",font=("times new roman", 16, "bold")).grid(row=2,pady=5)
    Label(master, text="Flight Arrival : ",font=("times new roman", 16, "bold")).grid(row=3, pady=5)
    Label(master, text="Flight Departure : ",font=("times new roman", 16, "bold")).grid(row=4, pady=5)
    Label(master, text="Journey Duration : ",font=("times new roman", 16, "bold")).grid(row=5, pady=5)
    Label(master, text="Cost : ",font=("times new roman", 16, "bold")).grid(row=6,pady=5)

    Message(master, text="NOTE : Enter the correct Flight Details", font=("times new roman", 17, "bold"), width=500, fg='blue').grid(row=27)

    flightId = Entry(master, text=textFlightId)
    flightTerm = Entry(master, text=textFlightTerm)
    flightname = Entry(master, text=textFlighname)
    arrival = Entry(master, text=textArrival)
    departure = Entry(master, text=textDeparture)
    duration = Entry(master, text=textDuration)
    cost = Entry(master, text=textCost)

    def done():
        texta = "{}".format(flightId.get())
        textb = "{}".format(flightTerm.get())
        textc = "{}".format(flightname.get())
        textd = "{}".format(arrival.get())
        texte = "{}".format(departure.get())
        textf = "{}".format(duration.get())
        textg = "{}".format(cost.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte, textf, textg)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation', autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Flight VALUES""" + str(dataa))
        db.commit()
        cursor.execute("""SELECT * FROM Flight;""")

        print(cursor.fetchall())

        db.close()

    def deleteFlight():
        deleteFli = Tk()
        deleteFli.geometry("700x400")
        deleteFli.title("Delete Flights")

        deleteFliInput = StringVar()

        Label(deleteFli, text="Flight ID: ",font=("times new roman", 16, "bold")).grid(row=0)

        Label(deleteFli, text="NOTE : Enter the valid Flight Id that to be deleted ",font=("times new roman", 13, "bold"), fg='blue').grid(row=5)

        fliDelete = Entry(deleteFli, text=deleteFliInput)

        fliDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation',
                                 autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Flight WHERE flightId=""" + str(dataa));

            cursor.execute("""SELECT * FROM Flight;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteFli, text="Done", command=delete, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=360)
    Buttong = Button(master, text="Delete Flight", command=deleteFlight, bg="red", fg="white",font=("arial black", 15, "bold")).place(x=20, y=430)

    flightId.grid(row=0, column=1, pady=8)
    flightTerm.grid(row=1, column=1, pady=8)
    flightname.grid(row=2, column=1, pady=8)
    arrival.grid(row=3, column=1, pady=8)
    departure.grid(row=4, column=1, pady=8)
    duration.grid(row=5, column=1, pady=8)
    cost.grid(row=6, column=1, pady=8)


def Essentials():
    master = Tk()
    master.geometry("500x500")
    master.title("Other Essentials")

    textPackage = StringVar()
    textFood = StringVar()
    textOrderid = StringVar()
    textDrinks = StringVar()
    textOrders = StringVar()

    Label(master, text="Package Weight: ",font=("times new roman", 16, "bold")).grid(row=0,pady=5)
    Label(master, text="Food: ",font=("times new roman", 16, "bold")).grid(row=1,pady=5)
    Label(master, text="Order-ID(Food): ",font=("times new roman", 16, "bold")).grid(row=2,pady=5)
    Label(master, text="Drinks: ",font=("times new roman", 16, "bold")).grid(row=3,pady=5)
    Label(master, text="Order-ID(Drinks): ",font=("times new roman", 16, "bold")).grid(row=4,pady=5)

    package_weight = Entry(master, text=textPackage)
    foods = Entry(master, text=textFood)
    ordid1 = Entry(master, text=textOrderid)
    drinks = Entry(master, text=textDrinks)
    ordid2 = Entry(master, text=textOrders)

    def done():
        texta = "{}".format(package_weight.get())
        textb = "{}".format(foods.get())
        textc = "{}".format(ordid1.get())
        textd = "{}".format(drinks.get())
        texte = "{}".format(ordid2.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Sharan@2003', db='Air_Reservation', autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO essential values""" + str(dataa));
        db.commit()

        cursor.execute("""SELECT * FROM essential;""")

        print(cursor.fetchall())

        db.close()

    # print('"{}"'.format(name.get()))
    # print(texta)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50", fg="white",font=("arial black", 15, "bold")).place(x=20, y=270)

    package_weight.grid(row=0, column=1)
    foods.grid(row=1, column=1)
    ordid1.grid(row=2, column=1)
    drinks.grid(row=3, column=1)
    ordid2.grid(row=4, column=1)


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x400")
app.title("LOGIN FORM")


def login():
    user_credentials = {
        "sharan": "01",
        "jawad": "07",
        "admin": "pass"
    }

    username = user_entry.get()
    password = user_pass.get()

    if username in user_credentials:
        if user_credentials[username] == password:
            tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
            login_successful()
        else:
            tkmb.showwarning(title='Wrong password', message='Please check your password')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


def login_successful():
    # Hide the login form
    root = tk.Tk()
    root.title("Air Reservation System")
    root.geometry("1000x800")
    root.config(bg="#F0F0F0")




    # Create and place the welcome label
    label = tk.Label(root, text="WELCOME TO THE AIR RESERVATION SYSTEM", font=("Algerian", 30, "bold"), fg="dark blue",bg="#F0F0F0")
    label.pack(pady=20)

    # Create buttons with creative colors and fonts
    myButtonb = tk.Button(root, text="Flights", command=flight, font=("arial black", 18, "bold"),fg="#FFFFFF",bg="#0052CC", activeforeground="#FFFFFF", activebackground="#003399")
    myButtonb.pack(pady=20)

    myButtonc = tk.Button(root, text="Tickets", command=ticket, font=("arial black", 18), fg="#FFFFFF", bg="#009933",
                          activeforeground="#FFFFFF", activebackground="#006600")
    myButtonc.pack(pady=20)

    myButtone = tk.Button(root, text="Passenger", command=passenger, font=("Arial black", 18), fg="#FFFFFF",
                          bg="#CC3300",activeforeground="#FFFFFF", activebackground="#993300")
    myButtone.pack(pady=20)

    myButtond = tk.Button(root, text="Other Essentials", command=Essentials, font=("Arial black", 18), fg="#FFFFFF",
                          bg="purple", activeforeground="#FFFFFF", activebackground="#990000")
    myButtond.pack(pady=20)

    root.mainloop()


label = ctk.CTkLabel(app, text="Welcome to SK Airlines",font=("Algerian", 18, "bold"))

label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='LOGIN',font=("arial black", 15, "bold"))
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

app.mainloop()


