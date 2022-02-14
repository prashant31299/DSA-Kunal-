def selectionsort(arr):
    for i in range(len(arr)):
        min=i

        for j in range (1,len(arr)):
            if arr[j]<arr[i]:
                min=j
        
        arr[i],arr[min] = arr[min],arr[i]


A = [64, 25, 12, 22, 11]

selectionsort(A )
print(A)