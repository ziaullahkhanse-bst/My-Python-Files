def divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count = count + 1
            else:
                count = count + 2
        i = i + 1
    return count

print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))
print(divisors(1))
print(divisors(100))