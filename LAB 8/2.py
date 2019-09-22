from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('stdrecord')
cur=con.cursor()


from Tkinter import *
root=Tk()
#root.geometry('840x420')



Label(root,text='Student Record Keeping System :',font='Times 20 bold').pack()
Label(root,text='Enter Student Er.No. :').pack()
Label(root,text='Enter First Name :').pack()
Label(root,text='Enter Last Name :').pack()
Label(root,text='Enter DOB :').pack()
Label(root,text='Enter Fathers Name :').pack()
Label(root,text='Select your Highest qualification : ').pack()
v2=IntVar()
v3=IntVar()
v4=IntVar()
Checkbutton(root,text='Btech',variable=v2,onvalue=10).pack()
Checkbutton(root,text='Mtech',variable=v3,onvalue=12).pack()
Checkbutton(root,text='Ph.D',variable=v4,onvalue=16).pack()

Label(root,text='Select your Branch : ').pack()
v1=IntVar()
r=Radiobutton(root,text='CSE',variable=v1,value=1)
r.pack()
r1=Radiobutton(root,text='ECE',variable=v1,value=2)
r1.pack()
r2=Radiobutton(root,text='ME',variable=v1,value=3)
r2.pack()
r3=Radiobutton(root,text='CE',variable=v1,value=4)
r3.pack()
r4=Radiobutton(root,text='CHE',variable=v1,value=5)
r4.pack()

Label(root,text='Select your Certification : ').pack()

v6=IntVar()
s=Radiobutton(root,text='CSE',variable=v6,value=1)
s.pack()
s1=Radiobutton(root,text='ECE',variable=v6,value=2)
s1.pack()
s2=Radiobutton(root,text='ME',variable=v6,value=3)
s2.pack()
s3=Radiobutton(root,text='CE',variable=v6,value=4)
s3.pack()

Label(root,text='Enter Registration date :').pack()
Label(root,text='Enter Student Address :').pack()
Label(root,text='Enter Student Mobile :').pack()
Label(root,text='Enter Student Email :').pack()
Label(root,text='Enter student CGPA :').pack()
Label(root,text='Enter Student Hobbies :').pack()

Label(root,text='Enter student id to fetch record :').pack()
a=Entry(root)
a.pack()
b=Entry(root)
b.pack()
c=Entry(root)
c.pack()
d=Entry(root)
d.pack()
e=Entry(root)
e.pack()
x=Entry(root)
x.pack()
p=Entry(root)
p.pack()
h=Entry(root)
h.pack()
i=Entry(root)
i.pack()
j=Entry(root)
j.pack()
k=Entry(root)
k.pack()

cur.execute("create table if not exists std1(stdcode number primary key, sfname varchar(20), slname varchar(20), dob varchar(10), fname varchar(20), course number(4), branch number(4), rdate varchar(10), stadd varchar(20), stm varchar(20), stmail varchar(20), stcg number(4), sthob varchar(20), stcert varchar(20))")

def insert():
    def func():
        if(v2.get()==10):
            x='Btech'
        elif(v3.get()==12):
            x='Mtech'
        elif(v4.get()==16):
            x='Phd'
        if(v1.get()==1):
            p='CSE'
        elif(v1.get()==2):
            p='ECE'
        elif(v1.get()==3):
            p='ME'
        elif(v1.get()==4):
            p='CE'
        elif(v1.get()==5):
            p='CHE'
        if(v6.get()==1):
            q='RHCE'
        elif(v6.get()==2):
            q='MCSE'
        elif(v6.get()==3):
            q='CCNA'
        elif(v6.get()==4):
            q='OCP'
    cur.execute("insert into std1 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(int(a.get()),b.get(),c.get(),d.get(),e.get(),x.get(),p.get(),h.get(),i.get(),j.get(),k.get(),int(l.get()),m.get(),q.get()))
    con.commit()
    showinfo('Information','Insertion Successful')

def show():
    a=[(int(d.get()))]
    cur.execute("select *from emp1 where empcode=?",a)
    t=cur.fetchall()
    showinfo('Result',t)
   # l=Label(root,text=t)
   # l.pack()

def showall():
    cur.execute("select *from emp1")
    t=cur.fetchall()
    lv=Label(root,text=t)
    lv.pack()

def delete():
    cur.execute("drop table emp1")
    t=cur.fetchall()
Button(root,text='Insert',command=insert).pack()
Button(root,text='Show',command=show).pack()
Button(root,text='Show all',command=showall).pack()
Button(root,text='Delete All Data',command=delete).pack()






root.mainloop()
