def increment_string(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    
    if tail == "":
        return s + "1"
    
    length = len(tail)
    new_number = str(int(tail) + 1).zfill(length)
    return head + new_number

print(increment_string("foo"))
print(increment_string("foobar23"))
print(increment_string("foo0042"))
print(increment_string("foo9"))
print(increment_string("foo099"))
print(increment_string(""))
print(increment_string("1"))