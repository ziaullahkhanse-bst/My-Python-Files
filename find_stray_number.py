def stray(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

print(stray([1, 1, 2]))
print(stray([17, 17, 3, 17, 17, 17, 17]))
print(stray([5, 5, 5, 5, 7]))
print(stray([10, 10, 10, 3, 10]))
print(stray([1, 1, 1, 1, 1, 1, 9]))