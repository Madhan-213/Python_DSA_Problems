arr = [10,20,30]
element =40
position = 3
arr.append(0)

for i in range(len(arr)-1,position,-1):
    if arr[i] == arr[i-1]:
        arr[position] =element
print("array after insert = ",arr)