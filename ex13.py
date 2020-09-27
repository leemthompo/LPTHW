from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("What kind of document do you require?:")
DocType = input()
message = "You have requested a {}. This can be delivered in 7 working days."
print(message.format(DocType))
