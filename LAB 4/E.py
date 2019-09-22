a=input('enter string a: ')
b=input('enter string b: ')
if(a.find(b)==-1):
    print 'not found'
else:
    l=a.find(b)
    print 'found at location : ',l
input()
