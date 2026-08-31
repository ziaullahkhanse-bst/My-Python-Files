def high_and_low(numbers):
    
    num_list = numbers.split()
    
    
    int_list = []
    for num in num_list:
        int_list.append(int(num))
    
    
    highest = max(int_list)
    lowest = min(int_list)
    
    
    return str(highest) + " " + str(lowest)


print(high_and_low("1 2 3 4 5"))        
print(high_and_low("1 2 -3 4 5"))       
print(high_and_low("1 9 3 4 -5"))       
print(high_and_low("42"))              