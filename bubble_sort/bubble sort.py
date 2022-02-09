from ssl import OPENSSL_VERSION_INFO


def bubbsort(arr):
    
    for i in range(len(arr)):

        for j in range(0, len(arr)-i-1):

            if arr[j] > arr[j+1] :
                arr[j] ,arr[j+1]=arr[j+1],arr[j]

arr=[3,5,32,45,22,34,535,342,2324]
bubbsort(arr)
print(arr)
