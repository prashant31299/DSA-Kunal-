def mergesort(arr):
    if len(arr) > 1:
        mid =len(arr)//2

        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)

        i=j=k=0
        while i < len(L) and j<len(R):
            if L[i] <R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]= R[j]
                j+=1
            k+=1
            

        # cheking left iteams
        while i< len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

arr=[123,123,322,21,23,4,11,109]
print(mergesort(arr))
print(arr)