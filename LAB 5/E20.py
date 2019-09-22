from Dictionary import D4,D1,D2,D3,D6,D5
x=input("Enter Name to search")
y=input("Enter\n1:Enrollment No\n2:Mobile No.\n3:City & State\n4:Email\n")
for i,j in D1.iteritems():
    if(x==j):
        if y==1:
            print '\nName:',x,'\nEnrollment No:',i
        elif y==2:
            print '\nName:',x,"\nMobile No.:",D3[i],
        elif y==3:
            print '\nName:',x,"\nCity:",D2[i]," State:",D4[i]
        elif y==4:
            print '\nName:',x,"\nEmail:",D6[i]
        else:
            print "No other details available of",x
