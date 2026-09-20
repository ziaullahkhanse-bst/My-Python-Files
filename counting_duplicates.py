def duplicate_count(text):
    text = text.lower()
    count = 0
    checked = []
    
    for char in text:
        if text.count(char) > 1 and char not in checked:
            count = count + 1
            checked.append(char)
    
    return count

print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))