arr=[2,3,4,2,4,2,]
unique = []
for num in arr:
    if num not in unique :
        unique.append(num)
print("array after removing duplication ",unique)