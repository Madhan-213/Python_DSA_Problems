arr = [1,2,3,4,5,6,7]
targat = 6
low = 0
high = len(arr)-1
found = False

while low < high :
    mid = (high+low)//2
    if arr[mid]==targat:
        print(f"element {targat} found at {mid}")
        found = True
        break
    elif arr[mid] <targat :
        low = mid + 1
    else:
        high = mid-1

if not found :
    print("array element not found ")