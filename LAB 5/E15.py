from Dictionary import D5,D1
a=0.0
p=[]
for i,j in D5.iteritems():
    
    if (j[0]+j[1]+j[2])/3.0 > a:
        a=(j[0]+j[1]+j[2])/3.0
        p=[]
        p.append(i)
    elif (j[0]+j[1]+j[2])/3.0==a:
        p.append(i)
print 'Highest average Score is',a,'Scored by :-'
for i in p:
    print i,D1[i]
	
