# Ask for note
note = input("Enter a note: ")

# Ask for filename
filename = input("Enter a file name: ")

# Open file for writing
file = open(filename, "w")

# Write note to file
file.write(note)

# Close file
file.close()

# Success message
print("Note saved successfully!")