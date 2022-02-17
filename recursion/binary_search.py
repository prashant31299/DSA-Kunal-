from ast import If


def binarysearch(arr,t,s,e):
    if s>e:
        return -1

    mid =s+(e-s)//2
    if (t==arr[mid]):
        return mid
    elif (t<arr[mid]):
        return binarysearch(arr,t,s,mid-1)
    else:
        return binarysearch(arr,t,mid+1,e)


arr=[2,3,4,5,6,77,444,888]
print(binarysearch(arr,888,0,len(arr)-1))