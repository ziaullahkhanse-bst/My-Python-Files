def to_jaden_case(string):
    words = string.split()
    result = []
    
    for word in words:
        result.append(word.capitalize())
    
    return " ".join(result)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
print(to_jaden_case("hello world"))
print(to_jaden_case("i am jaden smith"))