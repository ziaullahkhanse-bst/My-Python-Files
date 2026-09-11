def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False
    
    squared = sorted([x * x for x in array1])
    sorted_array2 = sorted(array2)
    
    return squared == sorted_array2

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([1, 2, 3], [1, 4, 9]))
print(comp([1, 2, 3], [1, 4, 10]))
print(comp([], []))
print(comp(None, [1, 4, 9]))