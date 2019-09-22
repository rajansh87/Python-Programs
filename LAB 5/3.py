a=[]
i=0
while i<10:
    n=input('enter elements : ')
    a.append(n)
    i=i+1
t=0
t=a[0]
a[0]=a[-1]
a[-1]=t
print a

input()
