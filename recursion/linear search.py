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
def findindexlist(arr,t,i,list):
    
    if (i==len(arr)):
        return list
    if arr[i]==t:
        list.append(i)

    findindexlist(arr,t,i+1,list)


list=[]
arr=[1,32,3,2,4,3,4,5,4,3,2,3,4,3,4,3,4,4,4,4,4,44,4]
print(findindexlist(arr,4,0,list))


