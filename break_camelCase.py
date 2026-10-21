def solution(s):
    result = ""
    for char in s:
        if char.isupper():
            result = result + " "
        result = result + char
    return result

print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))
print(solution("helloWorld"))
print(solution("breakCamelCase"))
print(solution("camelCasingTest"))