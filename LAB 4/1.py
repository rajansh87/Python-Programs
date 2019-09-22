sa=input('enter total amount in your saving account : ')
ca=input('enter total amount in your current account : ')
ch=input('for saving account press s, for current account press c ')
if(ch=='s'):
    en=input('press w for withdrawal and d for deposit : ')
    if(en=='w'):
        a=input('enter amount to withdraw : ')
        if((sa-a)>=1000):
            sa=sa-a
            print '\n\n*********withdrawal completed**********\n\n'
            print 'your saving account balance is ',sa
        else:
            print '\n\n*********insufficient balance**********\n\n'
    elif(en=='d'):
        b=input('enter amount to deposit : ')
        sa=sa+b
        print 'your saving account balance is ', sa
    else:
        print '\n\n******wrong selection******\n\n'
elif(ch=='c'):
    en=input('press w for withdrawal and d for deposit : ')
    if(en=='w'):
        a=input('enter amount to withdraw : ')
        if((ca-a)>=10000):
            ca=ca-a
            print '\n\n*********withdrawal completed**********\n\n'
            print 'your current account balance is ',ca
        else:
            print '\n\n*********insufficient balance**********\n\n'
    elif(en=='d'):
        b=input('enter amount to deposit : ')
        ca=ca+b
        print 'your current account balance is ', ca
    else:
        print '\n\n******wrong selection******\n\n'
else:
    print '\n\n*******wrong selection*******\n\n'
input()
    
