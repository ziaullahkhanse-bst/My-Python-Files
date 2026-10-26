def reverse_words(text):
    words = text.split(" ")
    result = []
    for word in words:
        result.append(word[::-1])
    return " ".join(result)

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))
print(reverse_words("The quick brown fox jumps over the lazy dog."))
print(reverse_words("a b c d"))
print(reverse_words(""))