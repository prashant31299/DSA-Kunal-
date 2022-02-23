#print n to 1 
"""def fun(n):
    if (n==0):
        return
    
    print(n)
    fun(n-1)

fun(5)"""

# print 1 to n
def reverse(n):
    if n==0:
        return
       
    print(n)

    reverse(n-1)
    print(n)
reverse(5)