import random

score = 0

for i in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct = num1 + num2
    
    try:
        answer = int(input(f"What is {num1} + {num2}? "))
        
        if answer == correct:
            print("Correct!")
            score = score + 1
        else:
            print(f"Wrong! The answer was {correct}")
            
    except ValueError:
        print("Please enter a number!")
    
    print()

print(f"Your score: {score} out of 5")