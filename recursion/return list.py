def findindexlist(arr,t,i,list):
    
    if (i==len(arr)):
        return list
    if arr[i]==t:
        list.append(i)

    
    return findindexlist(arr,t,i+1,list)


A=[]
arr=[1,2,3,4,2,4,2]
print(findindexlist(arr,2,0,A))
