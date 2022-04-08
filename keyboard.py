from tkinter import*
import tkinter as tk
from tkinter import ttk

#function
exp=" "
def press(num):
    global exp
    exp+=str(num)
    aqua.set(exp)

def clear():
    global exp
    exp=" "
    aqua.set(exp)

def action():
    global exp
    exp="Next Line:"
    aqua.set(exp)



key=tk.Tk()
key.title("Screen Keyboard")
#size of keyboard
key.geometry("1010x250")
key.maxsize(width=1260,height=220)
key.minsize(width=1260,height=220)
#background
key.configure(bg="darkred")
#phtot icon
key.iconbitmap("icn.ico")


#entry box
aqua=tk.StringVar()
entry=ttk.Entry(key,state="readonly",textvariable=aqua)
entry.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)

#Def

def shift():
    pass

def tab():
    pass
#Button keyboard
#first line
q=ttk.Button(key,text="Q",command=lambda:press("Q")).grid(row=1,column=0)
w=ttk.Button(key,text="W",command=lambda:press("W")).grid(row=1,column=1)
e=ttk.Button(key,text="E",command=lambda:press("E")).grid(row=1,column=2)
r=ttk.Button(key,text="R",command=lambda:press("R")).grid(row=1,column=3)
t=ttk.Button(key,text="T",command=lambda:press("T")).grid(row=1,column=4)
y=ttk.Button(key,text="Y",command=lambda:press("Y")).grid(row=1,column=5)
u=ttk.Button(key,text="U",command=lambda:press("U")).grid(row=1,column=6)
i=ttk.Button(key,text="I",command=lambda:press("I")).grid(row=1,column=7)
o=ttk.Button(key,text="O",command=lambda:press("O")).grid(row=1,column=8)
p=ttk.Button(key,text="P",command=lambda:press("P")).grid(row=1,column=9)
cur=ttk.Button(key,text="[",command=lambda:press("[")).grid(row=1,column=10)
cur_c=ttk.Button(key,text="]",command=lambda:press("]")).grid(row=1,column=11)
back_slash=ttk.Button(key,text="\\",command=lambda:press("\\")).grid(row=1,column=12)


clear=ttk.Button(key,text="Clear",width=20,command=clear).grid(row=1,column=13)

#second line
a=ttk.Button(key,text="A",command=lambda:press("A")).grid(row=2,column=0)
s=ttk.Button(key,text="S",command=lambda:press("S")).grid(row=2,column=1)
d=ttk.Button(key,text="D",command=lambda:press("D")).grid(row=2,column=2)
f=ttk.Button(key,text="F",command=lambda:press("F")).grid(row=2,column=3)
g=ttk.Button(key,text="G",command=lambda:press("G")).grid(row=2,column=4)
h=ttk.Button(key,text="H",command=lambda:press("H")).grid(row=2,column=5)
j=ttk.Button(key,text="J",command=lambda:press("J")).grid(row=2,column=6)
k=ttk.Button(key,text="K",command=lambda:press("K")).grid(row=2,column=7)
l=ttk.Button(key,text="L",command=lambda:press("L")).grid(row=2,column=8)
semi_co=ttk.Button(key,text=";",command=lambda:press(";")).grid(row=2,column=9)
d_colon=ttk.Button(key,text='"',command=lambda:press('"')).grid(row=2,column=10)
enter=ttk.Button(key,text="Enter",width=35,command=action).grid(row=2,columnspan=150)

#third line
z=ttk.Button(key,text="Z",command=lambda:press("Z")).grid(row=3,column=0)
x=ttk.Button(key,text="X",command=lambda:press("X")).grid(row=3,column=1)
c=ttk.Button(key,text="C",command=lambda:press("C")).grid(row=3,column=2)
v=ttk.Button(key,text="V",command=lambda:press("V")).grid(row=3,column=3)
b=ttk.Button(key,text="B",command=lambda:press("B")).grid(row=3,column=4)
n=ttk.Button(key,text="N",command=lambda:press("N")).grid(row=3,column=5)
m=ttk.Button(key,text="M",command=lambda:press("M")).grid(row=3,column=6)
left=ttk.Button(key,text="<",command=lambda:press("<")).grid(row=3,column=7)
right=ttk.Button(key,text=">",command=lambda:press(">")).grid(row=3,column=8)
slash=ttk.Button(key,text="/",command=lambda:press("/")).grid(row=3,column=9)
q_mark=ttk.Button(key,text="?",command=lambda:press("?")).grid(row=3,column=10)
coma=ttk.Button(key,text=",",command=lambda:press(",")).grid(row=3,column=11)
dot=ttk.Button(key,text=".",command=lambda:press(".")).grid(row=3,column=12)
shift=ttk.Button(key,text="Shift",width=20,command=shift).grid(row=3,column=13)

#fourth line
ctrl=ttk.Button(key,text="Ctrl",command=lambda:press("Ctrl")).grid(row=4,column=0)
fn=ttk.Button(key,text="Fn",command=lambda:press("Fn")).grid(row=4,column=1)
wimdow=ttk.Button(key,text="Window",command=lambda:press("Window")).grid(row=4,column=2)
alt=ttk.Button(key,text="Alt",command=lambda:press("Alt")).grid(row=4,column=3)
space=ttk.Button(key,text="Space",width=50,command=lambda:press(" ")).grid(row=4,columnspan=12)
Alt_gr=ttk.Button(key,text="Alt Gr",command=lambda:press("Alt Gr")).grid(row=4,column=8)
open_b=ttk.Button(key,text="(",command=lambda:press("(")).grid(row=4,column=9)
close_b=ttk.Button(key,text=")",command=lambda:press(")")).grid(row=4,column=10)
tab=ttk.Button(key,text="Tab",command=tab).grid(row=4,column=11)


#fifth line
exclamation_mark=ttk.Button(key,text="!",command=lambda:press("!")).grid(row=5,column=0)
at=ttk.Button(key,text="@",command=lambda:press("@")).grid(row=5,column=1)
number=ttk.Button(key,text="#",command=lambda:press("#")).grid(row=5,column=2)
dollar=ttk.Button(key,text="$",command=lambda:press("$")).grid(row=5,column=3)
percent=ttk.Button(key,text="%",command=lambda:press("%")).grid(row=5,column=4)
caret=ttk.Button(key,text="^",command=lambda:press("^")).grid(row=5,column=5)
symbol=ttk.Button(key,text="&",command=lambda:press("&")).grid(row=5,column=6)
star=ttk.Button(key,text="*",command=lambda:press("*")).grid(row=5,column=7)
minus=ttk.Button(key,text="-",command=lambda:press("-")).grid(row=5,column=8)
plus=ttk.Button(key,text="+",command=lambda:press("+")).grid(row=5,column=9)
equal=ttk.Button(key,text="=",command=lambda:press("=")).grid(row=5,column=10)


#sixth line
one=ttk.Button(key,text="1",command=lambda:press("1")).grid(row=6,column=0)
two=ttk.Button(key,text="2",command=lambda:press("2")).grid(row=6,column=1)
three=ttk.Button(key,text="3",command=lambda:press("3")).grid(row=6,column=2)
four=ttk.Button(key,text="4",command=lambda:press("4")).grid(row=6,column=3)
five=ttk.Button(key,text="5",command=lambda:press("5")).grid(row=6,column=4)
six=ttk.Button(key,text="6",command=lambda:press("6")).grid(row=6,column=5)
seven=ttk.Button(key,text="7",command=lambda:press("7")).grid(row=6,column=6)
eight=ttk.Button(key,text="8",command=lambda:press("8")).grid(row=6,column=7)
nine=ttk.Button(key,text="9",command=lambda:press("9")).grid(row=6,column=8)
zero=ttk.Button(key,text="0",command=lambda:press("0")).grid(row=6,column=9)


key.mainloop()
