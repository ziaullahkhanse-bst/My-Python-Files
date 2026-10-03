def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    return sum(arr) - min(arr) - max(arr)

print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([1, 2]))
print(sum_array([5]))
print(sum_array([]))
print(sum_array(None))