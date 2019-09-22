from std_record import d3,d1
s={98: 'Airtel', 77:'Reliance', 99:'Vodafone'}
for x,y in s.iteritems():
    print '\n\nUsers of',y,'are:-\n'
    for i,j in d3.iteritems():       
        if j.startswith(str(x)):
            print i,d1[i]
	 
