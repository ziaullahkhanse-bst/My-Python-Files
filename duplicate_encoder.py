def duplicate_encode(word):
   
    word = word.lower()
    
    result = ""
    
    for char in word:
        if word.count(char) == 1:
            result = result + "("
        else:
            result = result + ")"
    
    return result


print(duplicate_encode("din"))        
print(duplicate_encode("recede"))     
print(duplicate_encode("Success"))    # ")())())"
print(duplicate_encode("(( @"))       # "))(("
