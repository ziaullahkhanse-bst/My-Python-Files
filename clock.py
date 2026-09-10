def past(h, m, s):
    
    total_seconds = (h * 3600) + (m * 60) + s
    total_milliseconds = total_seconds * 1000
    return total_milliseconds

# Test
print(past(0, 1, 1))    
print(past(1, 0, 0))    
print(past(0, 0, 1))    # 1000
print(past(1, 30, 0))   # 5400000
