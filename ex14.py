from sys import argv

script, user_name = argv
prompt = 'type here please>> '

print(f"Hi {user_name}, I'm the {script} script. ")
print("I'd like to ask you a series of questions. ")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

# {} is called the format activator

print(f"""
Alright, so you said {likes} to liking meself.
You live in {lives}. Me not sure where that is. And you have a {computer} computer. Nice!
""")
