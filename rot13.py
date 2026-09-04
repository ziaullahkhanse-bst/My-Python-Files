def rot13(text):
    result = ""
    
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Check if uppercase or lowercase
            if char.isupper():
                # Shift uppercase letter
                shifted = ord(char) + 13
                if shifted > ord('Z'):
                    shifted = shifted - 26
                result = result + chr(shifted)
            else:
                # Shift lowercase letter
                shifted = ord(char) + 13
                if shifted > ord('z'):
                    shifted = shifted - 26
                result = result + chr(shifted)
        else:
            # Keep non-letters as they are
            result = result + char
    
    return result

# Test
print(rot13("Hello"))        # Uryyb
print(rot13("Uryyb"))        # Hello
print(rot13("Hello World!")) # Uryyb Jbeyq!