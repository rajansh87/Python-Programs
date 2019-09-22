from Tkinter import *
from tkMessageBox import *
root=Tk()
Label(root,text='click on button ').pack()
def fun():
    showinfo('hi','good morning')
    showerror('error','something went wrong')
    askyesno('response','do you agree')
    askyesnocancel('response','do you agree')
Button(root,text='click',command=fun).pack()
root.mainloop()
