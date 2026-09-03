def unique_in_order(sequence):
    result = []
    
    for item in sequence:
        if len(result) == 0 or item != result[-1]:
            result.append(item)
    
    return result

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
print(unique_in_order(''))
print(unique_in_order([]))