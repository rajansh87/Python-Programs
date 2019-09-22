from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('500x700')
Label(root,text='enter num1').pack()
a=Entry(root)
a.pack()
Label(root,text='enter num2').pack()
b=Entry(root)
b.pack()
                                   
def sum():
    s=(int(a.get())+int(b.get()))
    Label(root,text=s).pack()
Button(root, text='add',command=sum).pack()

def sub():
    m=(int(a.get())-int(b.get()))
    Label(root,text=m).pack()
Button(root, text='subtract',command=sub).pack()

def mul():
    n=(int(a.get())*int(b.get()))
    Label(root,text=n).pack()
Button(root, text='multiply',command=mul).pack()

def div():
    p=(float(a.get())/float(b.get()))
    Label(root,text=p).pack()
Button(root, text='divide',command=div).pack()

root.mainloop()
