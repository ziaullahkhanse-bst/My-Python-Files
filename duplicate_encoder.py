def duplicate_encode(word):
    # Convert to lowercase first (ignore case)
    word = word.lower()
    
    result = ""
    
    for char in word:
        if word.count(char) == 1:
            result = result + "("
        else:
            result = result + ")"
    
    return result

# Test
print(duplicate_encode("din"))        # "((("
print(duplicate_encode("recede"))     # "()()()"
print(duplicate_encode("Success"))    # ")())())"
print(duplicate_encode("(( @"))       # "))(("