tuple = (1, 2, 3, 4, 5)
def avg(tuple):
    sum = 0
    for i in tuple:
        sum += i
    return sum / len(tuple)
print(avg(tuple))
