def reverse_seq(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result

print(reverse_seq(5))
print(reverse_seq(3))
print(reverse_seq(1))