note = input("Enter a note: ")

filename = input("Enter a file name: ")

file = open(filename, "w")

file.write(note)

# Close file
file.close()

# Success message
print("Note saved successfully!")
