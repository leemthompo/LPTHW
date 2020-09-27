# Exercise 18: Names, Variables, Code, Functions

# This function is like the previous argv scripts

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#zero arguments
def print_none():
    print("I don't have arguments now please fuck off. Oh I see, said the witch.I never got the letters. I guess I'll get a new pair. She stepped forward and knelt beside the bed. The woman was still wearing a pair of clothes so that she could have access to the letters she'd stolen from the attic. Are you alright, Miss she asked. Her voice was cold and there wasn't a hint of her usual smile in it. I sighed and let myself get up. I looked at the witch and I realized what was going through my mind. She had no place here at all. This was some kind of hell that she was sent to. How had she been able to keep her sanity when the other witch had just sent herself out in a flimsy disguise and had started to walk around with a wand in hand? There seemed to be a whole world out there that I wanted to find and help but couldn't find. No, never mind, it had to be the other witch's fault that she was being forced to do this..")

print_two("Jack", "Paterson")
print_two_again("Pat", "Jackerson")
print_one("First!")
print_none()
