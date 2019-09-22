i=0
max=0
while i<10:
    r=input('enter no')
    if r%2!=0 and r>max:
        max=r
    i=i+1
print "Largest odd no was=",max
input()
