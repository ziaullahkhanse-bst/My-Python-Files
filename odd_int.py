def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

print(find_it([7]))
print(find_it([0]))
print(find_it([1,1,2]))
print(find_it([0,1,0,1,0]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))