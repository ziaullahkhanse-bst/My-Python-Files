def descending_order(num):
    
    digits = list(str(num))
    
   
    digits.sort(reverse=True)
    
    
    return int("".join(digits))


print(descending_order(42145))        
print(descending_order(145263))       
print(descending_order(123456789))    
print(descending_order(0))            
print(descending_order(111))          