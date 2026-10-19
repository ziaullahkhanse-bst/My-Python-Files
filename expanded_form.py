def expanded_form(num):
    num_str = str(num)
    result = []
    length = len(num_str)
    
    for i in range(length):
        digit = int(num_str[i])
        if digit != 0:
            place_value = digit * (10 ** (length - i - 1))
            result.append(str(place_value))
            
    return " + ".join(result)

print(expanded_form(12))
print(expanded_form(45))
print(expanded_form(70304))
print(expanded_form(9000000))
print(expanded_form(1))
print(expanded_form(10502))