from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('500x700')
Label(root,text='enter temperature in celsius : ').pack()
a=Entry(root)
a.pack()

                                   
def temp():
    b=float(a.get())
    tf=(b*1.8)+32
    Label(root,text=tf).pack()
Button(root,text='temperature in fahrenheit : ',command=temp).pack()

Label(root,text='enter temperature in fahrenheit : ').pack()
c=Entry(root)
c.pack()

                                   
def temp2():
    e=float(c.get())
    tc=(e-32)/1.8
    Label(root,text=tc).pack()
Button(root,text='temperature in celsius : ',command=temp2).pack()

root.mainloop()
