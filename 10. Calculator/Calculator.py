#Function for calculator app
def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    should_accumulate = True
    num1 = float(input("Enter number 1: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter number 2: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Should you wish to perform more calculation with {answer}?: | 'yes' or 'no'").lower()

        if should_continue == "yes":
            num1 = answer
        else:
            should_accumulate = False
            calculator()

calculator()