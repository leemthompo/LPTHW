# LINES 2-4 USES ARGV TO GET A FILENAME.
import sys
from sys import argv

script, filename = argv
txt = open(filename)

# I added this meself. With the len(sys.argv) function you can count the number of arguments.

print("Number of arguments: ", len(sys.argv))

print(f"Here's your {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
