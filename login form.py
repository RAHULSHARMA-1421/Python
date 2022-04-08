from tkinter import*
from tkinter import messagebox, ttk
from PIL import Image, ImageTk



tk = Tk()
tk.geometry("1000x600")
tk.title("Login Form")
tk.configure(background="lightblue")
frame=Frame(tk)
frame=Frame(tk,bg="black",width=600,height=200)
frame.place(x=200,y=126)


#title label
lb1title=Label(text="Login System",font=("arial",30,"bold"),fg="black").pack(pady=40
                                                                             )


#label

Label(frame,text="Username",font=("arial",15,"bold"),bg="green").place(x=120,y=50)
Label(frame,text="password",font=("arial",15,"bold"),bg="green").place(x=120,y=90)


#Entry
username=StringVar()
password=StringVar()

e_username=Entry(frame,textvariable=username,width=20,bd=3)
e_username.place(x=280,y=50)
e_password=Entry(frame,textvariable=password,width=20,bd=3,show="*")
e_password.place(x=280,y=90)

#button
Button(frame,text="Login",height="1",width=12,bg="red",fg="white",bd=0).place(x=120,y=150)
Button(frame,text="Reset",height="1",width=12,bg="red",fg="white",bd=0).place(x=250,y=150)
Button(frame,text="Exit",height="1",width=12,bg="red",fg="white",bd=0,command=tk.destroy).place(x=380,y=150)


               
tk.mainloop()
