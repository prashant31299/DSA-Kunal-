def sumoftringle(A):
    if len(A)<1:
        return 
        # base condition 

    temp=[0]*(len(A)-1)
    for i in range (0,len(A)-1):
        x= A[i]+A[i+1]
        temp[i]=x
    
    sumoftringle(temp)

    print(A)

A=[1,2,3,4,5]
sumoftringle(A)
