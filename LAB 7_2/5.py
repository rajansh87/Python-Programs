from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('500x700')
Label(root,text='Your Personal Details').pack()
Label(root,text='enter your name: ').pack()
a=Entry(root)
a.pack()
Label(root,text='enter your DoB in DD/MM/YYYY: ').pack()
b=Entry(root)
b.pack()

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
    Label(root,text='You are '+a.get()+' '+x+' '+p).pack()
Button(root,text='See Details',command=func).pack()




root.mainloop()
