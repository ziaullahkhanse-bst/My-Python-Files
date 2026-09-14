def array_diff(a, b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result

print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))
print(array_diff([1, 2, 3], [1, 2]))
print(array_diff([1, 2, 3], []))
print(array_diff([], [1, 2]))