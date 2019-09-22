from Tkinter import *
root=Tk()
root.geometry('500x600')

def fun():
   Button(root,text="go",command=fun2).pack()
def fun2():
    Label(root,text="Nice Job").pack()
Button(root, text="create",command=fun).pack()
root.mainloop()
