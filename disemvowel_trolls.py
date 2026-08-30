def disemvowel(string_):
    vowels = "aeiouAEIOU"  
    result = ""  
    
    for char in string_:
        if char not in vowels:
            result = result + char  
    
    return result


print(disemvowel("This website is for losers LOL!"))  
print(disemvowel("Hello World"))                      
print(disemvowel("aeiou"))                            