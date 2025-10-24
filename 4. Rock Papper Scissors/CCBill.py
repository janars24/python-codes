import random

name = input("Enter the list of people you dined separated with a space: ").split()

name1 = random.choice(name)

print(f"The person who has to pay the bill is {name1}")
