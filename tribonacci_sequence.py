def tribonacci(signature, n):
    # If n is 0, return empty list
    if n == 0:
        return []
    
    # Start with the signature (first 3 numbers)
    result = signature[:]  # Copy the signature
    
    # Keep adding numbers until we have n numbers
    while len(result) < n:
        # Add the last 3 numbers
        next_num = result[-1] + result[-2] + result[-3]
        result.append(next_num)
    
    # Return first n numbers
    return result[:n]

# Test
print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10))  # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([1, 2, 3], 5))   # [1, 2, 3, 6, 11]
print(tribonacci([1, 1, 1], 0))   # []