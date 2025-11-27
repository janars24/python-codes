print("Welcome to Love Calculator")
print("**************************")


def true_love(name1, name2):
    combinedName = name1 + name2
    combinedName = combinedName.lower()
    print(combinedName)

    t = combinedName.count("t")
    r = combinedName.count("r")
    u = combinedName.count("u")
    e = combinedName.count("e")
    firstDigit = t + r + u + e
    l = combinedName.count("l")
    o = combinedName.count("o")
    v = combinedName.count("v")
    e = combinedName.count("e")
    secondDigit = l + o + v + e

    score = int(str(firstDigit) + str(secondDigit))
    print(f"Your love score is {score}%")

a = input("Enter name1: ")
b = input("Enter name2: ")

true_love(a, b)