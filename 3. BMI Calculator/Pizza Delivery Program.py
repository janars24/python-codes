print("********************")
print("Build your PIZZA!!!!")
print("********************")

sizeOfPizza = input("What size of pizza do you want? S, M, or L ").lower()
pepperoni = input("do you wish to add pepperoni on your pizza? (Y/N)").lower()
cheese = input("do you wish to add extra cheese on your pizza? (Y/N)").lower()
price = 0

if sizeOfPizza == "s":
    price += 10
elif sizeOfPizza == "m":
    price += 15
elif sizeOfPizza == "l":
    price += 20
else:
    print("Select a valid pizza size")

if pepperoni == "y":
    if sizeOfPizza == "s":
        price += 2
    else:
        price += 3

if cheese == "y":
    price += 2

print(f"Your total amount of your order is ${price}")