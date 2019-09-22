def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=input('enter a no. : ')
b=input('enter a no. : ')
c=input('enter a no. : ')

m=max(a,b,c)
print 'largest no. is ',m
input()
