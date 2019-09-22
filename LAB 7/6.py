from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('200x300')
Label(root,text='hello', font='Times 20 bold',fg='red',bg='yellow').pack()
Label(root,text='enter your first name').pack()

name=Entry(root)
name.pack()

Label(root,text='enter your last name').pack()

lname=Entry(root)
lname.pack()

def fun():
    Label(root,text='Welcome '+name.get()+' '+lname.get()).pack()
Button(root, text='submit',command=fun).pack()




root.mainloop()
