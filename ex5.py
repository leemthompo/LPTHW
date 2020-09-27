name = 'Liam Mottio'
age = 32 # true
height = 80 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'Whitish'
hair = 'Brown'

cms = height * 30
kgs = weight * 2.2

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. That's {cms} centimeters.")
print(f"He's {weight} pounds heavy. That's {round(kgs)} kilograms.")
print(f"Actually that's not that heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
