def is_palindrome(a):
    b=a[::-1]
    if(b==a):
        return 'yes'
    else:
        return 'no'

a=input('enter string : ')
p=is_palindrome(a)
print p
input()
