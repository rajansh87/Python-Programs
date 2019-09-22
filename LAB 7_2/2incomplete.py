from Tkinter import *
root=Tk()
root.title('my Gui')
root.geometry('500x700')
Label(root,text='enter number : ').pack()
a=Entry(root)
a.pack()

                                   
def check(n):
    f=0
    i=2
    while(i<=n/2):
        if(n%i==0):
            f=1
            break
        i=i+1
    if(f==0):
        Label(root,text='prime no. ').pack()
    else:
        Label(root,text='not a prime no. ').pack()
    
Button(root,text='check : ',command=check(a.get())).pack()



root.mainloop()
