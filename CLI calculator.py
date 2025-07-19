def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

while True:
    print("\n--- Simple CLI Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter operator (+, -, *, /): ")
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator! Please use +, -, *, or /.")
            continue
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != 'yes':
        print("Goodbye!")
        break
