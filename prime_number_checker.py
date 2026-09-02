def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check if any number divides evenly
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a divisor, not prime
    
    return True  # No divisors found, it's prime

# Test
print(is_prime(1))    # False
print(is_prime(2))    # True
print(is_prime(3))    # True
print(is_prime(4))    # False
print(is_prime(10))   # False
print(is_prime(17))   # True
print(is_prime(-5))   # False