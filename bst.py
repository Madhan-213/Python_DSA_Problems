#bst
arr=[1,2,3,4,5]
target=3
high = len(arr)-1
low=0
found = False

while low <= high:
    mid = (high+low)//2
    if arr[mid] == target:
        print("elemrnt found")
        found= True
        break
    elif arr[mid] < target:
        low = mid+1
    else:
        high = mid -1
if not found:
    print("element not found")
