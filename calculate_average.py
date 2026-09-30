def find_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0

print(find_average([3, 4, 5, 2, 1]))
print(find_average([9, 5, 3, 4, 7]))
print(find_average([]))