from std_record import d5,d1
a=0
p=[]
for i,j in d5.iteritems():       
    if j[0]>a:
        a=j[0]
        p=[]
        p.append(i)
    elif j[0]==a:
        p.append(i)
print 'Highest Score in Physics is',a,'Scored by :-'
for i in p:
    print i,d1[i]
	
