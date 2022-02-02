def pick(arr):
    left = 1                  # first element cant be peak
    right = len(arr)-2        # last element cant be peak
    
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid] < arr[mid+1]:
            left = mid + 1
        elif arr[mid-1] > arr[mid] > arr[mid+1]:
            right = mid - 1
    
    return mid

arr = [0,10,33,5,4,3,2]
print(pick(arr))