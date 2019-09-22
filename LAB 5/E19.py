def Sum(n):
    s=0
    while(n!=0):
        d=n%10
        n=n/10
        s=s+d
    return s
def Prime(a):
    i=2
    while i<=a**0.5:
        if a%i==0:
            return 0
        i=i+1
    return 1
def Ma():
    i=57
    a={}
    while i<=100:
        if (Prime(i)==1):
            x=i
            y=Sum(i)
            d={x:y}
            a.update(d)
        i=i+1
    print a
Ma()
