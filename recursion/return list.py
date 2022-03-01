def findindexlist(arr,t,i,list):
    if (i==len(arr)):
        return list
    if arr[i]==t:
        list.append(i)
    
    return findindexlist(arr,t,i+1,list)


A=[]
arr=[2,2,2,3,1,2,3,2]
print(findindexlist(arr,3,0,A))
