from Dictionary import D5,D1
a=0
p=[]
for i,j in D5.iteritems():       

    if j[2]>a:
        a=j[2]
        p=[]
        p.append(i)
    elif j[2]==a:
        p.append(i)
print 'Highest Score in Maths is',a,'Scored by :-'
for i in p:
    print i,D1[i]
	
