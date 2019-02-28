from sys import argv

# Get the filename
script, filename = argv

# Opens the file and sets it to a variable
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# This allows users to call another file
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
