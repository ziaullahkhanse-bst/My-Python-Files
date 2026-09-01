a = input("Enter a fileName: ")

b = input("Enter a text to add: ")

file = open(a, "a")

file.write(b + "\n")  

file.close()

print("Text added successfully!"
