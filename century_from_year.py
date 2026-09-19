def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(2742))
print(century(1))
print(century(100))
print(century(101))