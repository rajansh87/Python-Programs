
def simple_interest(a,r,t):
    si=a*r*t/100
    return si
a,r,t=input('enter amount ,rate, time : ')
ans=simple_interest(a,r,t)
print 'simple interest = ',ans
input()

