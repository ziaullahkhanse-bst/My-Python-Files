def sum_array(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(sum_array([1, 5.2, 4, 0, -1]))
print(sum_array([-2.398]))
print(sum_array([]))
print(sum_array([10, 20, 30]))
print(sum_array([1.5, 2.5, 3.5]))
print(sum_array([-5, -10, -15]))