numbers = []
even_numbers = []

for i in range(10):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)
    
    if num % 2 == 0:
        even_numbers.append(num)

print("All numbers:", numbers)
print("Even numbers:", even_numbers)