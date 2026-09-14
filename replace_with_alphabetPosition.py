def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return " ".join(result)

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("abc"))
print(alphabet_position("hello"))
print(alphabet_position("123"))
print(alphabet_position(""))