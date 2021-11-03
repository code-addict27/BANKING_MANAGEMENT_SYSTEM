from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import login as log
#import p6 as p
import project_first_screen as p2
import withdraw as w
import deposit as d
import checkbalance as c
import search as s



def get_window3():
    window2.destroy()
    #window3 = Tk()
    #window1.quit()
    #window3.title("REGISTER SCREEN")
    #window3.geometry("1375x720+1+1")
    #window3.configure(width=200, height=72, bg="#C0C0C0")
    #window3.mainloop()
    s.search_information()
    return
def get_window4():
    window2.destroy()
    #window3 = Tk()
    #window1.quit()
    #window4.title("REGISTER SCREEN")
    #window4.geometry("1375x720+1+1")
    #window4.configure(width=200, height=72, bg="#C0C0C0")
    #window4.mainloop()
    w.withdraw_money()
    return
def get_window5():
    window2.destroy()
    d.deposit_money()
    return

def get_window6():
    window2.destroy()
    c.check_balance()
    return


def main_window():
    def get_window2():
        window2.destroy()

        # window2 = Tk()
        # window1.quit()
        # window2.title("LOGIN SCREEN")
        # window2.geometry("1375x720+1+1")
        # window2.configure(width=200, height=72, bg="#C0C0C0")

        p2.register_screen_1()
        return

    window2 = Tk()
    window2.title("WELCOME TO PYTHON BANK")
    window2.geometry("1375x720+0+0")
    window2.configure(width=200, height=72, bg="palegoldenrod")

    # frame=Frame(window2,bg="sky blue").pack()
    # canvas2 for left operation section
    canvas2a = Canvas(window2, width=500, height=730, bg="orchid")
    line1 = canvas2a.create_line(0, 0, 500, 0, fill="yellow", width=170)
    canvas_Label1 = Label(window2, text="     Functions  :", font=("Arial Bold", 30), bg="yellow").place(x=10, y=10)
    # my_img1 = ImageTk.PhotoImage(Image.open(("C:\\Users\\GULSHAN BANO\\Pictures\\images1.jpg")))
    withdraw_button = Button(window2, text=" Register account ", font=("Gadugi", 30), bg="white", fg="midnightblue",
                             width=15, command=get_window2).place(x=75, y=94)
    withdraw_button2 = Button(window2, text="    Withdraw    ", command=get_window4, font=("Gadugi", 30),
                              bg="light pink", fg="midnightblue", width=15).place(x=75, y=217)
    withdraw_button3 = Button(window2, text="      Deposit     ", command=get_window5, font=("Gadugi", 30),
                              bg="aquamarine", fg="red", width=15).place(x=75, y=337)
    withdraw_button4 = Button(window2, text="      Search   ", font=("Gadugi", 30), bg="khaki1", fg="midnightblue",
                              width=15, command=get_window3).place(x=75, y=460)
    withdraw_button5 = Button(window2, text="   Check Balance  ", font=("Gadugi", 30), bg="brown1", fg="snow2",
                              width=15, command=get_window6).place(x=75, y=582)
    canvas2a.place(x=0, y=0)

    # canvas2b for right search operation
    canvas2b = Canvas(window2, width=880, height=250, bg="OliveDrab2")
    welcome = Label(window2, text="**********Welcome to Python Bank*********", font=("Verdana Bold", 20), fg="white",
                    bg="OliveDrab2").place(
        x=580, y=95)

    # search = Label(window2, text=" Search   ", font=("Verdana Bold", 35), bg="OliveDrab2", fg="blue").place(x=540, y=50)
    # entry_search = ttk.Entry(window2, width=42, font=("Arial", 12)).pack(side=RIGHT, ipady=10, anchor=NE, pady=65,padx=120)
    # search_types = ("Name", "Account number", "Mobile number", "ID number")
    # combo = Combobox(window2, values=search_types, width=28, font=("Arial", 18))
    # combo.set("select")
    # combo.place(x=860, y=130)
    # Search1 = Button(window2, text="      search    ", font=("Gadugi", 15), bg="khaki1", fg="midnightblue", width=15,command = get_window7).place(x=800, y=180)

    canvas2b.place(x=501, y=0)

    # canvas2c = Canvas(window2, width=880, height=450, bg="azure2")
    # canvas2c.place(x=501, y=260)
    window2.mainloop()

#def welcome_page():
main_window()



