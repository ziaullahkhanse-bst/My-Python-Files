def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

print(lovefunc(1, 4))
print(lovefunc(2, 2))
print(lovefunc(0, 1))
print(lovefunc(0, 0))
print(lovefunc(5, 5))
print(lovefunc(3, 8))