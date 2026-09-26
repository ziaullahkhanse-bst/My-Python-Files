def persistence(num):
    count = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product = product * int(digit)
        num = product
        count = count + 1
    return count

print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(25))
print(persistence(77))
print(persistence(1234))