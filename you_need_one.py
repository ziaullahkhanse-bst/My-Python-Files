def check(a, x):
    return x in a

print(check([1, 2, 3, 4, 5], 3))
print(check([1, 2, 3, 4, 5], 6))
print(check(["apple", "banana", "orange"], "banana"))
print(check(["apple", "banana", "orange"], "grape"))
print(check([10, 20, 30], 10))
print(check([], 5))