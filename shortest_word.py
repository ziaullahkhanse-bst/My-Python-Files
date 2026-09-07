def find_short(s):
    # Split string into words
    words = s.split()
    
    # Find the shortest word length
    shortest = min(len(word) for word in words)
    
    return shortest

# Test
print(find_short("hello world"))              # 5
print(find_short("the quick brown fox"))      # 3
print(find_short("a b c"))                    # 1
print(find_short("python is fun"))            # 2 (is)