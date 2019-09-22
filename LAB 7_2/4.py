from Tkinter import *
root=Tk()
Label(root,text='radiobutton').pack()
Label(root,text='Select : ').pack()
v1=IntVar()
r=Radiobutton(root,text='red',variable=v1,value=1)
r.pack()
r1=Radiobutton(root,text='yellow',variable=v1,value=2)
r1.pack()
r2=Radiobutton(root,text='purple',variable=v1,value=3)
r2.pack()
def choice():
    if(v1.get()==1):
        Label(root,text='red').pack()
    elif(v1.get()==2):
        Label(root,text='yellow').pack()
    elif(v1.get()==3):
        Label(root,text='purple').pack()
Button(root,text='choice',command=choice).pack()
root.mainloop()
