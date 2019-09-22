from Dictionary import D5,D1
a=0
p=[]
for i,j in D5.iteritems():       

    if j[1]>a:
        a=j[1]
        p=[]
        p.append(i)
    elif j[1]==a:
        p.append(i)
print 'Highest Score in Chemistry is',a,'Scored by :-'
for i in p:
    print i,D1[i]
	
