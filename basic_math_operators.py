def basic_op(operator,value1,value2):
    if operator=="+":
        result=value1+value2
        return result
    elif operator=="-":
        result=value1-value2
        return result
    elif operator=="*":
        result=value1*value2
        return result
    elif operator=="/":
        result=value1/value2
        return result
    else:
        return None

print(basic_op('+', 4, 7)) 
print(basic_op('-', 15, 18)) 
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))