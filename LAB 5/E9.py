a={'1111E36':'mp','1111E37':'up','1111E38':'ap', '1111E39':'ap', '1111E40':'ap', '1111E41':'mp'}
b=[]
for i,j in a.iteritems():
    if j not in b:
        print j
        for k,l in a.iteritems():
            if j==l:
                print k
input()
