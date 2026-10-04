def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)

print(two_sum([1, 2, 3], 4))
print(two_sum([3, 2, 4], 6))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([1, 5, 3, 7, 2], 9))
print(two_sum([10, 20, 30, 40], 70))