def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

print(count_by(1, 10))
print(count_by(2, 5))
print(count_by(3, 4))
print(count_by(5, 3))
print(count_by(10, 2))