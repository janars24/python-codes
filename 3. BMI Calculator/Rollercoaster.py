print("Welcome to Roller Coaster ride")
height = int(input("Enter your height in centimetres: "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 7
        print(f"Your ticket price is {bill}")
    elif age <=17:
        bill = 12
        print(f"Your ticket price is {bill}")
    elif 45 <= age <= 55:
        print("You get a free ride")
    else :
        bill = 18
        print(f"Your ticket price is {bill}")

    photo = input("Do you want a photo (Y/N): ")
    if photo == "Y" :
        bill += 3
    print(f"your final bill is ${bill}")
else :
    print("Sorry, You cannot ride the roller coaster, GROWUP!")