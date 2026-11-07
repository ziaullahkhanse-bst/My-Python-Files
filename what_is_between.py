def between(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i)
    return result

print(between(1, 4))
print(between(2, 8))
print(between(-3, 3))
print(between(10, 10))