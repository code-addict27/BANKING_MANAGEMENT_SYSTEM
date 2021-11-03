from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime
import time
import pymysql as py
db = py.connect(user = 'root',password ='12345',host = 'localhost',database = 'customer_register')
my_cursor = db.cursor()

def search_information():
    def print_data(event=""):
        root = Tk()
        font1 = "arial", 12, "bold", "underline"
        font2 = "helvetica", 12
        root.geometry("500x500")

        entry_value = input.get()
        print(entry_value)
        combo_input = combo.get()
        print(combo_input)
        if (combo_input=="account number"):
            my_cursor.execute("SELECT * FROM customer_data8 where Account_no = %s ", (entry_value))
            #my_cursor.execute("SELECT * FROM customer_data where Ac_holder_name LIKE %s", (entry_value,))
            result = my_cursor.fetchall()
            print(result)
            index = 1
            for rec in result:
                print(rec)
                Label(root, text=rec[0]).grid(row=index, column=0)
                Label(root, text=rec[1]).grid(row=index, column=1)
                Label(root, text=rec[2]).grid(row=index, column=2)
                Label(root, text=rec[3]).grid(row=index, column=3)
                index = index + 1

        elif(combo_input == "name"):

            my_cursor.execute("SELECT * FROM customer_data8 where Ac_holder_name = %s ", (entry_value))
            result = my_cursor.fetchall()
            index = 1
            for rec in result:
                print(rec)
                Label(root, text=rec[0]).grid(row=index, column=0)
                Label(root, text=rec[1]).grid(row=index, column=1)
                Label(root, text=rec[2]).grid(row=index, column=2)
                Label(root, text=rec[3]).grid(row=index, column=3)
                index = index + 1




        elif(combo_input == "address(permanent)"):
            my_cursor.execute("SELECT * FROM customer_data8 where per_address = %s ", (entry_value))
            result = my_cursor.fetchall()

            index = 1
            for rec in result:
                Label(root, text=rec[0]).grid(row=index, column=0)
                Label(root, text=rec[1]).grid(row=index, column=1)
                Label(root, text=rec[2]).grid(row=index, column=2)
                Label(root, text=rec[3]).grid(row=index, column=3)
                index = index +1


        elif(combo_input == "mobile number"):
            my_cursor.execute("SELECT * FROM customer_data8 where mobile_no = %s ", (entry_value))
            result = my_cursor.fetchall()
            index = 1
            for rec in result:
                Label(root, text=rec[0]).grid(row=index, column=0)
                Label(root, text=rec[1]).grid(row=index, column=1)
                Label(root, text=rec[2]).grid(row=index, column=2)
                Label(root, text=rec[3]).grid(row=index, column=3)
                index = index + 1
        elif(combo_input == "ID number"):
            my_cursor.execute("SELECT * FROM customer_data8 where id_number = %s ", (entry_value))
            result = my_cursor.fetchall()
            total = my_cursor.rowcount
            print("Total Data ",str(total))
            index = 1
            for rec in result:
                Label(root, text=rec[0]).grid(row=index, column=0)
                Label(root, text=rec[1]).grid(row=index, column=1)
                Label(root, text=rec[2]).grid(row=index, column=2)
                Label(root, text=rec[3]).grid(row=index, column=3)
                index = index + 1
        root.mainloop()

    root1 = Tk()
    font1 = "arial", 12, "bold", "underline"
    font2 = "helvetica", 12
    root1.geometry("500x500")

    search_types = ("name", "account number", "address(permanent)", "mobile number", "ID number")
    combo = Combobox(root1, values=search_types,state="readonly", width=20)
    combo.set("select")
    combo.place(x=130, y=50)
    #global input
    input = StringVar()
    label = Label(root1, text="Search By", font=font1).place(x=40, y=50)
    entry1 = Entry(root1, font=font2, textvariable=input)
    #print(print_data())
    entry1.bind("<Return>", print_data)
    entry1.place(x=300, y=50)
    root1.geometry("500x500")
    button = Button(root1, text="Search", fg="green", command=print_data)
    button.place(x=100,y=100)
    root1.mainloop()

#search_information()

