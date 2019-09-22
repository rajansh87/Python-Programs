from std_record import d6
b=[]
user=input('enter email domain : ')
for a,b in d6.iteritems():
    if user==b.split('@')[1]:
        print a
        
input()
