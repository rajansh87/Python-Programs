from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('200x300')
Label(root,text='hello', font='Times 20 bold',fg='red',bg='yellow').pack()

Entry(root).pack()


Button(root, text='GO').pack()




root.mainloop()

