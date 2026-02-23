#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
       

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
   
arr=[30,10,20,90,30,60,11,1]
print("before sorting:",arr)
selection_sort(arr)
print("after sorting:",arr)


