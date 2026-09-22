def quarter_of(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    else:
        return 4

print(quarter_of(1))
print(quarter_of(2))
print(quarter_of(3))
print(quarter_of(4))
print(quarter_of(5))
print(quarter_of(6))
print(quarter_of(7))
print(quarter_of(8))
print(quarter_of(9))
print(quarter_of(10))
print(quarter_of(11))
print(quarter_of(12))