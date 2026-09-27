def digitize(n):
    result = []
    for digit in str(n):
        result.append(int(digit))
    return result[::-1]

print(digitize(35231))
print(digitize(0))
print(digitize(12345))
print(digitize(9876543210))