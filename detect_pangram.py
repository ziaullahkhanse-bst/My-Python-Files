def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    
    for char in alphabet:
        if char not in s:
            return False
            
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))
print(is_pangram("Pack my box with five dozen liquor jugs."))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("The quick brown fox jumps over the lazy dog 123!"))