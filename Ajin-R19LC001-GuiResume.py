from tkinter import *
from tkinter import messagebox as Msg

# import tkinter

SupWdwVar = Tk()

SupWdwVar.title("Tut Tul")

# SupWdwVar.geometry("800x800")

SupWdwVar.minsize(400, 300)

SupWdwVar.configure(background="white")

PflPicVar = PhotoImage("frank.gif")

Label(SupWdwVar,
      text="LogIn",
      font="Cambria 32 bold",
      bg="white", fg="black",
      width=40, height=2).grid(row=1, column=0, columnspan=2)





Label(SupWdwVar,
      text="EmailID : ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E,
      width=35, height=1).grid(row=4, column=0, sticky=W)

Repa = Entry(SupWdwVar,
             font="Times",width=70,
             bg="white", fg="grey")
Repa.insert(0,"Ex: ajin@yahoo.com")

Repa.grid(row=4, column=1, sticky=W)

Label(SupWdwVar,
      text="Password: ",
      font="Cambria 16 bold",
      fg="black",width=35,
      anchor=E, height=1).grid(row=5, column=0,sticky=W)

Repd=Entry(SupWdwVar,
     font="Times",show="*",width=70,     bg="white", fg="grey")

Repd.grid(row=5, column=1, sticky=W)

Userinfo = {}
def Not():
    Textq = Repa.get()
    Textw = Repd.get()

    if("@" not in Textq):
        Msg.showerror("Error","Enter Valid Email ID")
        return
    elif(len(Textw) < 8):
        Msg.showerror("Error","Invalid Password")
        return

    if(Textq== Userinfo["Email"] and Textw == Userinfo["Password"]):
        Msg.showinfo("Success", "you have logged in")
    else:
        Msg.showinfo("Error", "Invalid login details")
Button(SupWdwVar, text="Submit", width=7,height = 0, command=Not, font="arial 40 bold").grid(row=6, columnspan=2)

LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.grid(row=7, column=0)

LblVar = Label(SupWdwVar, text="*** \t OR \t ***", font="arial 16 bold")
LblVar.grid(row=8, columnspan=2)

LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.grid(row=9, column=0)

Label(SupWdwVar,
      text="Signup",
      font="Cambria 32 bold",
      bg="white", fg="black",
      width=40, height=2).grid(row=10, column=0, columnspan=2)


Label(SupWdwVar,
      text="Name : ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E,
      width=35, height=1).grid(row=11, column=0, sticky=E)

RegNamBoxVar= Entry(SupWdwVar,
             font="Cambria 16 bold",width=50,
             bg="white", fg="black")
RegNamBoxVar.grid(row=11, column=1, sticky=W)

Label(SupWdwVar,
      text="Enter Mobile: ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E,
      width=35, ).grid(row=12, column=0, sticky=E)

RegMblBoxVar = Entry(SupWdwVar,width=50,fg="grey", font="Times")
RegMblBoxVar.insert(0,"Ex: 956653465")
RegMblBoxVar.grid(row=12, column=1,sticky=W)

Label(SupWdwVar,
      text="Enter Email: ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E,
      width=35, height=1).grid(row=13, column=0, sticky=E)

RegMylBoxVar = Entry(SupWdwVar, font="Times",fg="grey",width=50)
RegMylBoxVar.insert(0,"Ex:ajin@yahoo.com")
RegMylBoxVar.grid(row=13, column=1,sticky=W)

Label(SupWdwVar,
      text="Password: ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E,width=35, height=1).grid(row=14, column=0, sticky=E)

RegPwdBoxVar = Entry(SupWdwVar, font="Times",width=50, show="*")
RegPwdBoxVar.insert(0,"Enter Password")
RegPwdBoxVar.grid(row=14, column=1,sticky=W)

Label(SupWdwVar,
      text="Repeat Password: ",
      font="Cambria 16 bold",
      fg="black",width=35,
      anchor=E, height=1).grid(row=15, column=0, sticky=E)

RptPwdBoxVar = Entry(SupWdwVar, width=50,font="Times", show="*")
RptPwdBoxVar.insert(0,"Repeat Password")
RptPwdBoxVar.grid(row=15, column=1,sticky=W)

def RegClickFnc():
    Userinfo["Name"] = RegNamBoxVar.get()
    if (Userinfo["Name"]) == "":
        Msg.showinfo("Error", "Name is missing")
        return
    Userinfo["Mobile"] = RegMblBoxVar.get()
    if len(Userinfo["Mobile"]) < 10 and type(Userinfo["Mobile"])!=int:
        Msg.showinfo("Error", "Invalid Mobile Number")
        return
    Userinfo["Email"] = RegMylBoxVar.get()
    if "@" not in Userinfo["Email"]:
        Msg.showerror("Error", "Enter Valid Email ID")
        return
    UsrPwdVar = RegPwdBoxVar.get()

    if (len(UsrPwdVar) < 8):
        Msg.showerror("Error", "Invalid Password")
        return
    RtpPwdVar = RptPwdBoxVar.get()
    if (len(RtpPwdVar) < 8):
        Msg.showerror("Error", "Invalid Password")
        return


    if(UsrPwdVar == RtpPwdVar):
        Userinfo["Password"] = UsrPwdVar
        Msg.showinfo("Success", "Registered Successfully")
    else:
        Msg.showerror("Error", "Password not match")

Button(SupWdwVar, text="Submit",
    bg="white", fg="black",
    width=10, command=RegClickFnc,
    font="arial 40 bold").grid(row=16, columnspan=2)






SupWdwVar.mainloop()

print("hello")
