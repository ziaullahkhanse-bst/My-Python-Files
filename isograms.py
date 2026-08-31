def is_isogram(string):
    string = string.lower()
    
    if len(string) == len(set(string)):
        return True
    else:
        return False

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram(""))
print(is_isogram("hello"))
print(is_isogram("world"))