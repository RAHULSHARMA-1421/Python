from tkinter import *
def final():
    if (e1.get()=="manpreet"):
        if (e2.get()=="1234"):
            world()
        else:print("invalid password")
    else:print("invalid username")
def quit():
    root.destroy()

root=Tk()
balance=5000

label1=Label(root,text="username")
label2=Label(root,text="password")

label1.grid(row=0)
label2.grid(row=1)

e1=Entry(root)
e2=Entry(root,show="*")

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(root,text="Login",command=final)
b1.grid(row=2,column=1)
b2=Button(root,text="Quit",command=quit)
b2.grid(row=2,column=2)

def world():
    root=Toplevel()
    global balance
    l1=Label(root,text="Initial balance :  "+ str(balance))
    l1.grid(row=0)

    
    def hello():
        l2=Label(root,text="Enter the amount : ")
        l2.grid(row=2)
        e3=Entry(root)
        e3.grid(row=2,column=1)
        def hello1():
            a=int(balance)+int(e3.get())
            l1.config(text="Initial balance : "+ str(a))
        b3=Button(root,text="Deposit done",command=hello1)
        b3.grid(row=3)
    b4=Button(root,text="Deposite",command=hello)
    b4.grid(row=1)



    def hello2():
        l3=Label(root,text="Enter the amount : ")
        l3.grid(row=2,column=2)
        e4=Entry(root)
        e4.grid(row=2,column=3)
        def hello3():
            global balance
            b=int(balance)-int(e4.get())
            l1.config(text="Initial balance : " +str(b))
        b5=Button(root,text="Withdrawal done",command=hello3)
        b5.grid(row=3,column=1)
    b6=Button(root,text="Withdrawal",command=hello2)
    b6.grid(row=1,column=3)
root.mainloop()
    
        
    
    
