print("*****************************")
print("Welcome to Bill Splitter app!")
print("*****************************")
totalBill = float(input("What was the total bill?\n$"))
tip = int(input("How much percentage you would like to tip?\n"))
noOfPersons = int(input("How many people to split the bill?\n"))
billWithTip = tip/100 * totalBill + totalBill
splittedBill = billWithTip/noOfPersons
finalAmount = round(splittedBill, 3)
print(f"Each of you should pay ${finalAmount}")
