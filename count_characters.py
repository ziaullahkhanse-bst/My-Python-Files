def count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result

print(count("aba"))
print(count(""))
print(count("hello"))
print(count("aabbcc"))
print(count("aaa"))