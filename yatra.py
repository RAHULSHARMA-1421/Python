from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
def quit():
    root.destroy()
root=Tk()
def message():
    messagebox.showerror('Error','wrong user name or password')


l1=Label(root,text='Welcome To Yatra.Com',fg='red')
l1.grid(row=0,columnspan=3)
l2=Label(root,text='username')
l2.grid(row=1)
l3=Label(root,text='password')
l3.grid(row=2)
e1=Entry(root)
e1.grid(row=1,column=1)
e2=Entry(root)
e2.grid(row=2,column=1)

b2=Button(root,text='quit',command=quit)
b2.grid(row=3,column=1)

def yatra():
    root=Toplevel()
    l1=Label(root,text='Welcome To Yatra',fg='red')
    l1.grid(row=0,columnspan=4)
    l2=Label(root,text='Chose Your Trip')
    l2.grid(row=1)
    def family():
        root=Toplevel()
        l1=Label(root,text='exciting offers on yatra!!')
        l1.grid(row=0,columnspan=4)
        l2=Label(root,text='chose trip')
        l2.grid(row=1)
        def domestic():
            root=Toplevel()
            l1=Label(root,text='Chose Destination')
            l1.grid(row=0,columnspan=4)
            def chandigarh():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake)')
                    l3.grid(row=2)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=10000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake ,rose garden)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=13000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake,rose garden,rock garden)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=18000 INR',command=platinum)
                b3.grid(row=3)
                
            b1=Button(root,text='Chandigarh',command=chandigarh)
            b1.grid(row=1)
            def himachal():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla)')
                    l3.grid(row=2)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=10000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla ,kufri)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=13000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla,kufri,mashobra)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=18000 INR',command=platinum)
                b3.grid(row=3)
            b2=Button(root,text='Himachal',command=himachal)
            b2.grid(row=2)
        b1=Button(root,text='Domestic',command=domestic)
        b1.grid(row=1,column=1)
        
        def international():
            root=Toplevel()
            l1=Label(root,text='Chose Destination')
            l1.grid(row=0,columnspan=4)
            def canada():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto)')
                    l3.grid(row=2)
                    l4=Label(root,text='flight tickets')
                    l4.grid(row=3)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=100000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto,nigra falls )')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=150000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto,nigra falls, british columbia)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=200000 INR',command=platinum)
                b3.grid(row=3)
                
            b1=Button(root,text='Canada',command=canada)
            b1.grid(row=1)
            def spain():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid)')
                    l3.grid(row=2)
                    l4=Label(root,text='flight tickets')
                    l4.grid(row=3)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=100000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid,barcelona)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=130000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid,barcelona,siville)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=200000 INR',command=platinum)
                b3.grid(row=3)
            b2=Button(root,text='Spain',command=spain)
            b2.grid(row=2)
        b2=Button(root,text='International',command=international)
        b2.grid(row=1,column=2)
        
    b1=Button(root,text='Family Trip',fg='green',command=family)
    b1.grid(row=1,column=1)
    def couple():
        root=Toplevel()
        l1=Label(root,text='exciting offers on yatra!!')
        l1.grid(row=0,columnspan=4)
        l2=Label(root,text='chose trip')
        l2.grid(row=1)
        def domestic():
            root=Toplevel()
            l1=Label(root,text='Chose Destination')
            l1.grid(row=0,columnspan=4)
            def chandigarh():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake),romantic night')
                    l3.grid(row=2)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=10000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake ,rose garden)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi,romantic night')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=13000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (sukhna lake,rose garden,rock garden)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi,romantic night')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=18000 INR',command=platinum)
                b3.grid(row=3)
                
            b1=Button(root,text='Chandigarh',command=chandigarh)
            b1.grid(row=1)
            def himachal():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla)')
                    l3.grid(row=2)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=10000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla ,kufri)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast and dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi,romantic night')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=13000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (shimla,kufri,mashobra)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner')
                    l4.grid(row=3)
                    l5=Label(root,text='wifi,romantic night')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=18000 INR',command=platinum)
                b3.grid(row=3)
            b2=Button(root,text='Himachal',command=himachal)
            b2.grid(row=2)
        b1=Button(root,text='Domestic',command=domestic)
        b1.grid(row=1,column=1)
        
        def international():
            root=Toplevel()
            l1=Label(root,text='Chose Destination')
            l1.grid(row=0,columnspan=4)
            def canada():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto),romantic night')
                    l3.grid(row=2)
                    l4=Label(root,text='flight tickets')
                    l4.grid(row=3)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=100000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto,nigra falls )')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast , dinner and romantic night')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=150000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (toronto,nigra falls, british columbia)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner and romantic night')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=200000 INR',command=platinum)
                b3.grid(row=3)
                
            b1=Button(root,text='Canada',command=canada)
            b1.grid(row=1)
            def spain():
                root=Toplevel()
                l1=Label(root,text='chose package')
                l1.grid(row=0,columnspan=4)
                def silver():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='3 star hotel for 2 nights and 3 dayswith couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid)')
                    l3.grid(row=2)
                    l4=Label(root,text='flight tickets')
                    l4.grid(row=3)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                    
                    
                
                b1=Button(root,text='Silver=100000 INR',command=silver)
                b1.grid(row=1)
                def gold():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='4 star hotel for 5 nights and 6 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid,barcelona)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast dinner and romantic night')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                        
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b2=Button(root,text='Gold=130000 INR',command=gold)
                b2.grid(row=2)
                def platinum():
                    root=Toplevel()
                    l1=Label(root,text='Your Package Includes:')
                    l1.grid(row=0)
                    l2=Label(root,text='5 star hotel for 7 nights and 8 days with couple suite')
                    l2.grid(row=1)
                    l3=Label(root,text='sight seeing (madrid,barcelona,siville)')
                    l3.grid(row=2)
                    l4=Label(root,text='Breakfast lunch dinner and romantic night')
                    l4.grid(row=3)
                    l5=Label(root,text='flight tickets')
                    l5.grid(row=4)
                    def confirm():
                        root=Toplevel()
                        l1=Label(root,text='total amount to be paid')
                        l1.grid(row=0)
                        e1=Entry(root)
                        e1.grid(row=0,column=2)
                        def done():
                            messagebox.showinfo('Successful!!','Booking Confirmed')
                            
                        b1=Button(root,text='Done',command=done)
                        b1.grid(row=1,column=2)
                    b1=Button(root,text='confirm',command=confirm)
                    b1.grid(row=3,column=1)
                    b2=Button(root,text='back')
                    b2.grid(row=3,column=2)
                b3=Button(root,text='Platinum=200000 INR',command=platinum)
                b3.grid(row=3)
            b2=Button(root,text='Spain',command=spain)
            b2.grid(row=2)
        b2=Button(root,text='International',command=international)
        b2.grid(row=1,column=2)
    b2=Button(root,text='Couple Trip',fg='orange',command=couple)
    b2.grid(row=1,column=2)
    
    

def login():
    if(e1.get()=='nitish'):
        if(e2.get()=='1234'):
            yatra()
        else:
            message()
    else:
        message

b1=Button(root,text='login',command=login)
b1.grid(row=3)
