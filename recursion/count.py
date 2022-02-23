import re


def count(n):
    return helper(n,0)

def helper(n,c):
    if n==0:
        return c
    
    rem= n%10
    if (rem==0):
        return helper(n/10,c+1)
    
    return helper(n/10, c)

print(count(1023012008))
