from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import time
import pymysql as py
db = py.connect(user = 'root',password ='12345',host = 'localhost',database = 'customer_register')
my_cursor = db.cursor()
global b











def check_balance():
    def display_content():
        global holder_name
        global account_num
        global mobile_num
        global id_num
        global avl_bal

        p_store = b.get()
        my_cursor.execute("SELECT * FROM customer_data8 where Account_no LIKE %s ", (p_store,))
        result = my_cursor.fetchall()
        for db in result:
            holder_name = db[0]
            account_num = db[1]
            mobile_num = db[7]
            id_num = db[11]
            avl_bal = db[14]

        Name = Label(window1, text="Name : ", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=220)
        Name_display = Label(window1, text=holder_name,bg="orchid").place(x=180, y=220)

        Account_No = Label(window1, text="Account_number :", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=280)
        Account_No_display = Label(window1, text=account_num,bg="orchid").place(x=180, y=280)

        Mobile_No = Label(window1, text="Mobile number:", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=330)
        Mobile_No_display = Label(window1, text=mobile_num,bg="orchid").place(x=180, y=330)

        Id_No = Label(window1, text="ID Number:", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=380)
        Id_No_display = Label(window1, text=id_num,bg="orchid").place(x=180, y=380)

        Avl_balance = Label(window1, text="Current amount :", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=430)
        Avl_balance_display = Label(window1, text=avl_bal,bg="orchid").place(x=180, y=430)

    window1 = Tk()
    window1.title("WELCOME TO PYTHON BANK")
    window1.geometry("1375x720+0+0")
    window1.configure(width=200, height=72, bg="palegoldenrod")

    canvas2a = Canvas(window1, width=600, height=730, bg="orchid")
    canvas2a.place(x=0, y=0)
    '''
    global TIME1
    TIME1=time.asctime()
    print(TIME1)
    #time1="global"
    #time1=datetime.date.today()
    #print(time1)
    '''

    global a
    a = StringVar()
    name = Label(window1, text="Name", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=30, y=30)
    name_entry = Entry(window1, textvariable=a,bg="orchid").place(x=90, y=30)
    global b
    b = StringVar()
    account_number = Label(window1, text="Account number", font=("Verdana Bold", 10),bg="orchid", fg="#00008B").place(x=270, y=30)
    account_number = Entry(window1, textvariable=b,bg="orchid").place(x=400, y=30)

    # account_entry1=Entry(window1,textvariable=b)
    # account_entry1.bind("<Return>",display_content)
    # account_entry1.place(x=380,y=30)
    display_button = Button(window1, text="Display Info", bg="palegoldenrod", font=("Verdana Bold", 10), command=display_content).place(
        x=250, y=80)
    info_label = Label(window1, text="According to above input - current balance and other customer data  ",
                       font=("Verdana Bold", 10), bg="orchid", fg="#00008B").place(x=40, y=140)
    window1.mainloop()

#check_balance()
