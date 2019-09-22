from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('500x700')
Label(root,text='enter ammount ').pack()
a=Entry(root)
a.pack()
Label(root,text='enter rate ').pack()
b=Entry(root)
b.pack()
Label(root,text='enter time ').pack()
c=Entry(root)
c.pack()
                                   
def si():
    s=(float(a.get())*float(b.get())*float(b.get()))
    Label(root,text=s).pack()
Button(root,text='simple interest ',command=si).pack()



root.mainloop()
