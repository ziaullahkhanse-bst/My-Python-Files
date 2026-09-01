note = input("Enter a note: ")

filename = input("Enter a file name: ")

file = open(filename, "w")

file.write(note)

file.close()

print("Note saved successfully!")
