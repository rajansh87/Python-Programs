a,b=input('Enter 2 nos.')
if a<b:
    t=a
    a=b
    b=t
r=1
while r>0:
    r=a%b
    a=b
    b=r
print a
    
input()
