# defining variable and assigning value 10
types_of_people = 10
# defining variable x, a string with an embedded variable
x = f"There are {types_of_people} types of people."

# defining variables
binary = "binary"
do_not = "don't"
# defining variable y, a string with 2 embedded variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
