a={'1111E36':'guna','1111E37':'bhopal','1111E38':'ujjain', '1111E39':'ujjain', '1111E40':'bhopal', '1111E41':'ujjain'}
b=[]
for i,j in a.iteritems():
    if j not in b:
        print j
        for k,l in a.iteritems():
            if j==l:
                print k
input()
