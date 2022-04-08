from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox, ttk


def login():
    user=username.get()
    code=password.get()

    if user=="Rahul" and code=="ravan1421":
        root=Toplevel(tk)
        root.geometry("800x600")
        root.title("Login Form")
        root.configure(bg="lightblue")


tk=Tk()
tk.geometry("800x600")
tk.title("Login Form")
tk.resizable(False,False)
global tk
global username
global password


#image add##
img = Image.open("rq.jpg") .resize((800, 600))
file = ImageTk.PhotoImage(img)
lb1=Label(tk,image=file)
lb1.pack()

#frame
frame=Frame(tk)
frame=Frame(tk,bg="black",width=400,height=340)
frame.place(x=50,y=200)

#label title
lb1title=Label(frame,text="Login System",font=("Impact",25,"bold"),fg="blue").place(x=110,y=30)

#label
Label(frame,text="Username",font=("arial",10,"bold"),bg="red").place(x=90,y=140)
Label(frame,text="Password",font=("arial",10,"bold"),bg="red").place(x=90,y=180)


#entry
username=StringVar()
password=StringVar()

e_username=Entry(frame,textvariable=username,width=20,bd=3)
e_username.place(x=180,y=140)
e_password=Entry(frame,textvariable=password,width=20,bd=3,show="*")
e_password.place(x=180,y=180)

#buttons
def reset():
    e_username.delete(0,END)
    e_password.delete(0,END)
Button(frame,text="Login",height="1",width=10,bg="red",fg="white",bd=0).place(x=80,y=240)
Button(frame,text="Reset",height="1",width=10,bg="red",fg="white",bd=0,command=reset).place(x=180,y=240)
Button(frame,text="Exit",height="1",width=12,bg="red",fg="white",bd=0,command=tk.destroy).place(x=280,y=240)




tk.mainloop()
