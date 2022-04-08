from tkinter import *
def quit():
    root.destroy()

root = Tk()

label_1=Label(root, text="username")
label_2=Label(root,text="password")

label_1.grid(row=0)
label_2.grid(row=1)

e1=Entry(root)
e2= Entry(root,show='*')

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(root,text="quit",command=quit)
b1.grid(row=2,column=2)
def technology():
    
    def tech():
        print(e1.get())
        print(e2.get())
        print(e3.get())
        print(e4.get())
    def radio():
        if(i.get()==1):
            print("male")
        else:
            print("female")
    def check():
        if(j.get()==1):
         print("c++")
        elif(j.get()==2):
         print("c++")
        elif(j.get()==3):
         print("java")
        else:
         print("python")
    def sunny():
        tech()
        radio()
        check()

    root = Toplevel()
    i=IntVar()
    j=IntVar()
    label_1=Label(root, text=" first name")
    label_2=Label(root,text="roll no.")
    label_3=Label(root,text="last name")
    label_4=Label(root,text="contact no.")
    label_5=Label(root,text="gender")
    label_6=Label(root,text="course")
    r1=Radiobutton(root,text="male",value=1,variable=i)
    r2=Radiobutton(root,text="female",value=2,variable=i)
    r3=Checkbutton(root,text="c",onvalue=1,variable=j)
    r4=Checkbutton(root,text="c++",onvalue=2,variable=j)
    r5=Checkbutton(root,text="java",onvalue=3,variable=j)
    r6=Checkbutton(root,text="python",onvalue=4,variable=j)


    label_1.grid(row=0)
    label_2.grid(row=1)
    label_3.grid(row=0,column=2)
    label_4.grid(row=1,column=2)
    label_5.grid(row=2)
    label_6.grid(row=3)
    r1.grid(row=2,column=1)
    r2.grid(row=2,column=2)
    r3.grid(row=3,column=1)
    r4.grid(row=3,column=2)
    r5.grid(row=3,column=3)
    r6.grid(row=3,column=4)

    e1=Entry(root)
    e2=Entry(root)
    e3=Entry(root)
    e4=Entry(root)

    e1.grid(row=0,column=1)
    e2.grid(row=0,column=3)
    e3.grid(row=1,column=1)
    e4.grid(row=1,column=3)
    b1=Button(root,text="submit",command=sunny)
    b1.grid(row=4,column=1)

def final():
    if(e1.get()=="webtech"):
        if(e2.get()=="1234"):
            technology()
        else:
            print("invalid password")
    else:
        print("invalid user")
bt2=Button(root,text="login",command=final)
bt2.grid(row=2,column=1)
                 

root.mainloop()
