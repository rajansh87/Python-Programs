from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('emprecord')
cur=con.cursor()
from Tkinter import *
root=Tk()
root.geometry('840x420')
l=Label(root,text='Employee Record Keeping System :',font='Times 20 bold')
l.grid(row=0,column=0)
l=Label(root,text='Enter Emp Code :')
l.grid(row=1,column=0)
l=Label(root,text='Enter First Name :')
l.grid(row=2,column=0)
l=Label(root,text='Enter Last Name :')
l.grid(row=3,column=0)
l=Label(root,text='Enter id to fetch record :')
l.grid(row=4,column=0)
a=Entry(root)
a.grid(row=1,column =1)
b=Entry(root)
b.grid(row=2,column =1)
c=Entry(root)
c.grid(row=3,column =1)
d=Entry(root)
d.grid(row=5,column =1)

cur.execute("create table if not exists emp1(empcode number primary key, efname varchar(20), elname varchar(20))")

def insert():
    cur.execute("insert into emp1 values(?,?,?)",(int(a.get()),b.get(),c.get()))
    con.commit()
    showinfo('Information','Insertion Successful')

def show():
    w=[(int(d.get()))]
    cur.execute("select *from emp1 where empcode=?",w)
    x=cur.fetchall()
    showinfo('Result',x)
   # l=Label(root,text=x)
   # l.grid(row=8,column=0)

def showall():
    cur.execute("select *from emp1")
    x=cur.fetchall()
    l=Label(root,text=x)
    l.grid(row=8,column=0)

def delete():
    cur.execute("drop table emp1")
  

Button(root,text='Insert',command=insert).grid(row=7,column =0)
Button(root,text='Show',command=show).grid(row=7,column =1)
Button(root,text='Show all',command=showall).grid(row=7,column =2)
Button(root,text='Delete All Data',command=delete).grid(row=7,column =6)






root.mainloop()
