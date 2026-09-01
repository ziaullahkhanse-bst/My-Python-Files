def find_uniq(arr):
    if arr[0] == arr[1]:
        common = arr[0]
    else:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]
    
    for num in arr:
        if num != common:
            return num

print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))
print(find_uniq([5, 5, 5, 5, 5, 5, 7]))