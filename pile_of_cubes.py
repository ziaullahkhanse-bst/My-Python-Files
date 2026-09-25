def find_nb(m):
    n = 1
    total = 0
    while total < m:
        total = total + n ** 3
        if total == m:
            return n
        n = n + 1
    return -1

print(find_nb(1071225))
print(find_nb(91716553919377))
print(find_nb(1))
print(find_nb(9))
print(find_nb(36))
print(find_nb(100))
print(find_nb(4183059834009))