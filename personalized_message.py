def greet(name, owner):
    if name==owner:
        return f"Hello boss"
    else:
        return f"Hello guest"

print(greet("Zia","Zia"))
print(greet("Ali","Zia"))




# Other Codes Below

# 1.
# def greet(name, owner):
#     return "Hello boss" if name == owner else "Hello guest"

# 2.
# def greet(name, owner):
#     return "Hello {}".format("boss" if name == owner else "guest")

# 3.
# def greet(name, owner):
#     return 'Hello '+['guest','boss'][name==owner]