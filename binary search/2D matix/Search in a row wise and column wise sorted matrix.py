
def rowcolume(arr,target):
    r=0
    c=len(arr)-1
    while r < len(arr) and c >=0:
        
        if arr[r][c]==target:
            return [ r,c]
        
        elif arr[r][c] < target:
            r+=1
        else:
            c-=1
    return [-1,-1]
mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
print(rowcolume(mat, 458,))
 