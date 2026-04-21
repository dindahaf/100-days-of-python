from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other three functions - subtract, multiply, and divide

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary

def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        user_operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        operator = operations[user_operator]
        answer = operator(num1, num2)
        print(f"{num1} {user_operator} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()




