def fact(a):
    i=1
    f=1
    while(i<=a):
        f=f*i
        i=i+1
    return f
n=input('enter number : ')
fa=fact(n)
print 'factorial of ',n ,'is ', fa
input()
