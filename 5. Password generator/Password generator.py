import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator")
nr_letters = int(input("Enter the no. of letters you want in password: "))
nr_numbers = int(input("Enter the no. of numbers you want in password: "))
nr_symbols = int(input("Enter the no. of symbols you want in password: "))

# password = ""
#
# for char in range (0, nr_letters):
#     password += random.choice(letters)
#
# for char in range (0, nr_numbers):
#     password += random.choice(numbers)
#
# for char in range (0, nr_symbols):
#     password += random.choice(symbols)
#
# print(f"Your password is {password}")

# Hard way

password_list = []

for char in range (0, nr_letters):
    password_list.append(random.choice(letters))

for char in range (0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"You password is {password}")
