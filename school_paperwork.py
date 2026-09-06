def paperwork(n, m):
    
    if n < 0 or m < 0:
        return 0
    else:
        return n * m


print(paperwork(5, 5))    
print(paperwork(-5, 5))   
print(paperwork(3, 4))    
print(paperwork(0, 5))    
print(paperwork(5, 0))    