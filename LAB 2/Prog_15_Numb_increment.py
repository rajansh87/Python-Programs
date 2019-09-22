r=input('enter no')
s=0
while r>0:
    d=r%10
    r=r/10
    if d!=9:
        s=s*10+d+1
    else:
        s=s*10
while s>0:
    d=s%10
    s=s/10
    r=r*10+d


print "Final no =",r
input()
