n=input('enter amount : ')
m=1
i=1
while m<=n:
    m=i*100
    i=i+1
m=m-100
i=i-2
print '100 rupee notes = ',i
x=n-m
a=1
j=1
while a<=x:
    a=j*50
    j=j+1
a=a-50
j=j-2
print '50 rupee notes = ',j
y=x-a
b=1
k=1
while b<=y:
    b=k*10
    k=k+1
b=b-10
k=k-2
print '10 rupee notes = ',k
input()


