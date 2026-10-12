def number(lines):
    result = []
    for i in range(len(lines)):
        result.append(str(i + 1) + ": " + lines[i])
    return result

print(number([]))
print(number(["a", "b", "c"]))
print(number(["hello"]))
print(number(["one", "two", "three", "four"]))