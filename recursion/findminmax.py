

def minrec(A,n):
    if (n==1):
        return A[0]
    return max(A[n-1],minrec(A,n-1))
    # this is search for min value 
    #return min (A[n-1],minrec(A,n-1))

A = [1, 4, 45, 6, -50, 10, 2]
n=len(A)
print(minrec(A,n))