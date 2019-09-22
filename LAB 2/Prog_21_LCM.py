a,b=input('Enter 2 nos.')
if a<b:
    t=a
    a=b
    b=t
r=1
i=1
while r==1:
    s=a*i
    if s%a==0 and s%b==0:
        break
    i=i+1
    

print s
input()    
