arr = [10,30,40,50]
max_element = arr[0]
for i in range(1,len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
print("maxium arr = ",max_element)