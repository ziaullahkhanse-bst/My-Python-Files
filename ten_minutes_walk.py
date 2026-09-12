def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    n = walk.count('n')
    s = walk.count('s')
    e = walk.count('e')
    w = walk.count('w')
    
    if n == s and e == w:
        return True
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))  
print(is_valid_walk(['n','s','e','w','n','s','e','w','n','s'])) 
print(is_valid_walk(['n','n','n','s','s','s','e','w','n','s']))  
print(is_valid_walk(['n','s','e','w','n','s','e','w']))          
print(is_valid_walk(['n','s','e','w','n','s','e','w','n','s','e'])) 