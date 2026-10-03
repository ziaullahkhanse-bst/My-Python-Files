def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            return True
        else:
            return False
    else:
        return False

print(is_triangle(1, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(2, 2, 2))
print(is_triangle(1, 2, 3))
print(is_triangle(-5, 1, 3))
print(is_triangle(0, 2, 3))
print(is_triangle(1, 2, 9))