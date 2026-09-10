def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total = total + num
    return total

print(positive_sum([1, -4, 7, 12]))
print(positive_sum([1, 2, 3, 4, 5]))
print(positive_sum([-1, -2, -3, -4, -5]))
print(positive_sum([]))
print(positive_sum([0, -1, 5, -3, 10]))