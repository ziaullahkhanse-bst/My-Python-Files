def get_count(sentence):
    vowels = "aeiou"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count = count + 1
    
    return count

# Test
print(get_count("hello"))        # 2
print(get_count("aeiou"))        # 5
print(get_count("abcde"))        # 2
print(get_count("my name"))      # 2
print(get_count("python"))       # 1