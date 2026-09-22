def find_even_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i
    return -1

print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
print(find_even_index([10, -80, 10, 10, 15, 35, 20]))
print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))
print(find_even_index([1, 2, 3, 4, 5, 6]))
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))