def find(arr,t,i):
    if (i==len(arr)):
        return False
    return arr[i]==t or find(arr,t,i+1)

arr=[1,23,232,242,234,54,232,324,2]
print(find(arr,23,0))

# how to find the index
def findindex(arr,t,i):
    if (i==len(arr)):
        return -1
    if arr[i]==t:
        return i 
    else:
        return findindex(arr,t,i+1)


# return thr array list on multiple recurserce 


