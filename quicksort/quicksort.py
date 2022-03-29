from tkinter import E


def partition(start,end,arr):
    pivotindex=start
    pivot = arr[pivotindex]

    while start < end:

        while start <len(arr) and arr[start] <= pivot:
            start +=1
        
        while arr[end] > pivot:
            end-=1

        
        if( start <end):
            arr[start] , arr[end] = arr[end] , arr[start]
