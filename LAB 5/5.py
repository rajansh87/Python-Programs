a=[]
i=0
while i<10:
    n=input('enter elements : ')
    a.append(n)
    i=i+1
a.sort()
print 'largest value is ',a[-1]
print 'smallest value is ',a[0]

input()
