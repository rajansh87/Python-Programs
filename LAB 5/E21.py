from Dictionary import D4,D1,D2,D3,D6,D5
x=input("Enter Enrollment to search")
for i,j in D1.iteritems():
    if(x==i):
        print '\nEnrollment No:',i,"\nName:",D1[i],"\nMobile No.:",D3[i],"\nCity:",D2[i]," State:",D4[i],"\nEmail:",D6[i]
