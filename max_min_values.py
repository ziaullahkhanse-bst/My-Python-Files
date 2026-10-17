def maximum(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def minimum(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

print("Max:", maximum([4, 6, 2, 1, 9, 63, -134, 566]))
print("Min:", minimum([4, 6, 2, 1, 9, 63, -134, 566]))
print("Max:", maximum([-52, 56, 30, 29, -54, 0, -110]))
print("Min:", minimum([-52, 56, 30, 29, -54, 0, -110]))
print("Max:", maximum([42, 54, 65, 87, 0]))
print("Min:", minimum([42, 54, 65, 87, 0]))
print("Max:", maximum([5]))
print("Min:", minimum([5]))