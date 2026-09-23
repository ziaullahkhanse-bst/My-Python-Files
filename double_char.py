def double_char(s):
    double=''.join([char*2 for char in s])
    return double

print(double_char("Zia"))
print(double_char("Khan"))
print(double_char("python"))