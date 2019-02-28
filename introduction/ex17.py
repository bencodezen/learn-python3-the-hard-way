from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file_data = open(from_file).read()

print(f"The input file is {len(in_file_data)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(in_file_data)

print("Alright, all done.")
