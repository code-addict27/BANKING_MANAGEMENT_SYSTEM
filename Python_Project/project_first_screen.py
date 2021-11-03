from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql as py
import os
import re
import random
import gullu as gu

db = py.connect(user = 'root',password ='12345',host = 'localhost',database = 'customer_register')
my_cursor = db.cursor()







def register_screen_1():
    def get_window1():
        window1.destroy()
        gu.main_window()


    def validateAllFields():
        if a.get() == "":
            messagebox.showinfo("Information", "please enter your full name to proceed")
        elif b.get() == "":
            messagebox.showinfo("Information", "please enter your father name")
        elif c.get() == "":
            messagebox.showinfo("Information", "please enter your mother name")
        elif int(d.get()) == 0:
            messagebox.showinfo("Information", "please enter your age")
        elif e.get() == "":
            messagebox.showinfo("Information", "please enter your DOB")
        elif f.get() == "":
            messagebox.showinfo("Information", "please enter your correct mobile no.")
        elif g.get() == "":
            messagebox.showinfo("Information", "please enter your permanent address")
        elif h.get() == "":
            messagebox.showinfo("Information", "please enter your temporary address")
        elif i.get() == "":
            messagebox.showinfo("Information", "please enter your id type")
        elif j.get() == "":
            messagebox.showinfo("Information", "please enter your id number")
        elif k.get() == "":
            messagebox.showinfo("Information", "please enter your account type")
        elif l.get() == "":
            messagebox.showinfo("Information", "please enter your current date")
        elif int(m.get()) == 0:
            messagebox.showinfo("Information", "please enter your deposit amount")
        else:
            messagebox.showinfo("Information", "User registered successfully")
    def create():
        enter_value()
        display_content()

        #display_content()
    def enter_value():
        name_input = a.get()
        father_input = b.get()
        mother_input = c.get()
        age_input = d.get()
        dob_input = e.get()
        mobile_input = f.get()
        permanent_address_input = g.get()
        temporary_address_input = h.get()
        id_type_input = i.get()
        id_number_input = j.get()
        account_type_input = k.get()
        date_account_input = l.get()
        combo_input = combo_value.get()
        account_no_input = random.randint(100000, 10000000000)
        deposit_amount_input = m.get()


        data_input = "INSERT INTO customer_data8 (Ac_holder_name,Account_no,gender,f_name,m_name,DOB,age,mobile_no,per_address,Tem_address,id_type,id_number,account_type,date_account_open,avl_bal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        append_record = (
            name_input, account_no_input, combo_input, father_input, mother_input, age_input, dob_input, mobile_input,
            permanent_address_input, temporary_address_input, id_type_input, id_number_input,
            account_type_input, date_account_input, deposit_amount_input)
        print(name_input, account_no_input, combo_input, father_input, mother_input, age_input, dob_input, mobile_input,
              permanent_address_input, temporary_address_input, id_type_input, id_number_input, account_type_input,
              date_account_input, deposit_amount_input)
        my_cursor.execute(data_input, append_record)
        db.commit()
        return

    def display_content():
        #enter_value()
        #validateAllFields()
        mobile_input = f.get()

        myquery = "SELECT Ac_holder_name,Account_no,gender,f_name,m_name,DOB,age,mobile_no,per_address,Tem_address,id_type,id_number,account_type,date_account_open,avl_bal FROM customer_data8 WHERE mobile_no = %s"
        myval = (mobile_input)

        my_cursor.execute(myquery, myval)
        result = my_cursor.fetchall()
        for mydb in result:
            name = mydb[0]
            account_num = mydb[1]
            gender = mydb[2]
            f_name = mydb[3]
            m_name = mydb[4]
            dobv = mydb[5]
            agev = mydb[6]
            mobile_num = mydb[7]
            p_address = mydb[8]
            t_address = mydb[9]
            id_type = mydb[10]
            id_num = mydb[11]
            account_type = mydb[12]
            date_account_open = mydb[13]
            avl_bal = mydb[14]

        Name = Label(window1, text="Name : ", bg="palegoldenrod").place(x=700, y=30)
        Name_display = Label(window1, text=name, bg="palegoldenrod", fg="#00008B").place(x=870, y=30)

        Gender = Label(window1, text="Gender : ", bg="palegoldenrod").place(x=700, y=90)
        Gender_display = Label(window1, text=gender, bg="palegoldenrod", fg="#00008B").place(x=870, y=90)

        Father_name = Label(window1, text="Father_name : ", bg="palegoldenrod").place(x=700, y=150)
        Father_name_display = Label(window1, text=f_name, bg="palegoldenrod", fg="#00008B").place(x=870, y=150)

        Mother_name = Label(window1, text="Mother_Name : ", bg="palegoldenrod").place(x=700, y=210)
        Mother_name__display = Label(window1, text=m_name, bg="palegoldenrod", fg="#00008B").place(x=870, y=210)

        DOB = Label(window1, text="Date of Birth : ", bg="palegoldenrod").place(x=700, y=270)
        DOB_display = Label(window1, text=dobv, bg="palegoldenrod", fg="#00008B").place(x=870, y=270)

        age = Label(window1, text="Age : ", bg="palegoldenrod").place(x=700, y=330)
        age_display = Label(window1, text=agev, bg="palegoldenrod", fg="#00008B").place(x=870, y=330)

        Mobile_No = Label(window1, text="Mobile number:", bg="palegoldenrod").place(x=700, y=390)
        Mobile_No_display = Label(window1, text=mobile_num, bg="palegoldenrod", fg="#00008B").place(x=870, y=390)

        Permanent_Address = Label(window1, text="Permanent_Address : ", bg="palegoldenrod").place(x=1000, y=30)
        Permanent_Address_display = Label(window1, text=p_address, bg="palegoldenrod", fg="#00008B").place(x=1170, y=30)

        Temporary_Address = Label(window1, text="Temporary_Address : ", bg="palegoldenrod").place(x=1000, y=90)
        Temporary_Address_display = Label(window1, text=t_address, bg="palegoldenrod", fg="#00008B").place(x=1170, y=90)

        Id_type = Label(window1, text="Id_type : ", bg="palegoldenrod").place(x=1000, y=150)
        Id_type_display = Label(window1, text=id_type, bg="palegoldenrod", fg="#00008B").place(x=1170, y=150)

        Id_No = Label(window1, text="ID Number:", bg="palegoldenrod").place(x=1000, y=210)
        Id_No_display = Label(window1, text=id_num, bg="palegoldenrod", fg="#00008B").place(x=1170, y=210)

        Account_type = Label(window1, text="Account_type:", bg="palegoldenrod").place(x=1000, y=270)
        Account_type_display = Label(window1, text=account_type, bg="palegoldenrod", fg="#00008B").place(x=1170, y=270)

        Date_account_open = Label(window1, text="Date_account_open:", bg="palegoldenrod").place(x=1000, y=330)
        Date_account_open_display = Label(window1, text=date_account_open, bg="palegoldenrod", fg="#00008B").place(
            x=1170,
            y=330)

        Account_num = Label(window1, text="Account Num : ", bg="palegoldenrod").place(x=1000, y=390)
        Account_num_display = Label(window1, text=account_num, bg="palegoldenrod", fg="#00008B").place(x=1170, y=390)

        Avl_balance = Label(window1, text="Current amount :", bg="palegoldenrod").place(x=1000, y=450)
        Avl_balance_display = Label(window1, text=avl_bal, bg="palegoldenrod", fg="#00008B").place(x=1170, y=450)

        db.commit()
        return

    window1 = Tk()
    window1.title("WELCOME TO PYTHON BANK")
    window1.geometry("1375x720+0+0")
    window1.configure(width=200, height=72, bg="palegoldenrod")

    canvas2a = Canvas(window1, width=600, height=730, bg="orchid")
    canvas2a.place(x=0, y=0)

    a = StringVar()
    name = Label(window1, text="Name", bg="orchid", fg="#00008B").place(x=30, y=30)
    name_entry = Entry(window1, textvariable=a, bg="orchid").place(x=120, y=30)

    b = StringVar()
    label_f_name = Label(window1, text="Father name", bg="orchid", fg="#00008B").place(x=30, y=70)
    father_entry = Entry(window1, textvariable=b, bg="orchid").place(x=120, y=70)

    c = StringVar()
    label_m_name = Label(window1, text="Mother name", bg="orchid", fg="#00008B").place(x=30, y=110)
    mother_entry = Entry(window1, textvariable=c, bg="orchid").place(x=120, y=110)

    d = IntVar()
    age = Label(window1, text="Age", bg="orchid", fg="#00008B").place(x=30, y=160)
    age_entry = Entry(window1, textvariable=d, bg="orchid").place(x=120, y=160)

    e = StringVar()
    label_dob = Label(window1, text="Date of Birth", bg="orchid", fg="#00008B").place(x=30, y=200)
    dob_entry = Entry(window1, textvariable=e, bg="orchid").place(x=120, y=200)

    f = IntVar()
    label_mobile_number = Label(window1, text="Mobile Number", bg="orchid", fg="#00008B").place(x=30, y=240)
    mobile_number_entry = Entry(window1, textvariable=f, bg="orchid").place(x=120, y=240)

    gender = Label(window1, text="Gender", bg="orchid", fg="#00008B").place(x=30, y=280)
    combo_value = StringVar()
    gender_value = ("Male", "Female", "other")
    combo = Combobox(window1, values=gender_value, textvariable=combo_value,
                     state="readonly")  # state prevent change in combo value
    combo.set("select")
    combo.place(x=120, y=280)

    g = StringVar()
    permanent_address = Label(window1, text="Permanent Address", bg="orchid", fg="#00008B").place(x=350, y=30)
    peramnent_address_entry = Entry(window1, textvariable=g, bg="orchid").place(x=460, y=30)

    h = StringVar()
    temporary_address = Label(window1, text="Temporary Address", bg="orchid", fg="#00008B").place(x=350, y=70)
    temporary_address_entry = Entry(window1, textvariable=h, bg="orchid").place(x=460, y=70)

    i = StringVar()
    id_type = Label(window1, text="Id Type", bg="orchid", fg="#00008B").place(x=350, y=110)
    id_type_entry = Entry(window1, textvariable=i, bg="orchid").place(x=460, y=110)

    j = StringVar()
    id_number = Label(window1, text="Id Number", bg="orchid", fg="#00008B").place(x=350, y=150)
    id_number_entry = Entry(window1, textvariable=j, bg="orchid").place(x=460, y=150)

    k = StringVar()
    account_type = Label(window1, text="Account Type", bg="orchid", fg="#00008B").place(x=350, y=200)
    account_type_entry = Entry(window1, textvariable=k, bg="orchid").place(x=460, y=200)

    l = StringVar()
    date_account_open = Label(window1, text="Current Date", bg="orchid", fg="#00008B").place(x=350, y=240)
    date_account_open_entry = Entry(window1, textvariable=l, bg="orchid").place(x=460, y=240)

    m = IntVar()
    deposit_amount = Label(window1, text="Deposit Amount", bg="orchid", fg="#00008B").place(x=350, y=280)
    deposit_amount_entry = Entry(window1, textvariable=m, bg="orchid").place(x=460, y=280)

    button = Button(window1, text="Create account", command=create, bg="palegoldenrod", fg="#00008B",
                    font=("Verdana Bold", 10)).place(x=100, y=350)
    button = Button(window1, text="Display account", command=get_window1, bg="palegoldenrod", fg="#00008B",
                    font=("Verdana Bold", 10)).place(x=270, y=350)
    window1.mainloop()
    return

#register_screen_1()