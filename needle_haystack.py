def find_needle(haystack):
    index = haystack.index("needle")
    return f"found the needle at position {index}"

# Test cases
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
# Output: found the needle at position 5

print(find_needle(["needle", "hay", "junk"]))
# Output: found the needle at position 0

print(find_needle(["hay", "junk", "needle"]))
# Output: found the needle at position 2