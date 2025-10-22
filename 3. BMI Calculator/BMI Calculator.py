print("BMI Calculator")

weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in centimeters: "))

bmi = weight / (height ** 2) * 10000
bmi = round(bmi, 2)

if bmi < 18.5 :
    print(f"your BMI is {bmi} and you are UNDERWEIGHT")
elif 18.5 <= bmi < 25 :
    print(f"Your BMI is {bmi} and you are NORMAL")
else :
    print(f"Your BMI is {bmi} and you're OVERWEIGHT")