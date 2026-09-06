def tribonacci(signature, n):
    if n == 0:
        return []
    result = signature[:]  
    
    while len(result) < n:
        next_num = result[-1] + result[-2] + result[-3]
        result.append(next_num)
    
    
    return result[:n]


print(tribonacci([1, 1, 1], 10))  
print(tribonacci([0, 0, 1], 10))  
print(tribonacci([1, 2, 3], 5))   
print(tribonacci([1, 1, 1], 0))   
