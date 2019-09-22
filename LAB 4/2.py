def fibo(n):
    a=0
    b=1
    c=1
    i=0
    while(i<n):
        a=b
        b=c
        print b
        c=a+b
        i=i+1

    
n=input('enter lenght of series : ')
fibo(n)
input()
