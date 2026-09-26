def grow(arr):
    result = 1
    for num in arr:
        result = result * num
    return result

print(grow([1, 2, 3, 4]))
print(grow([5, 3, 2]))
print(grow([10, 2]))
print(grow([7]))
print(grow([1, 1, 1, 1]))