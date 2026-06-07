def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        print("Thank you!")
        break

    elif choice == "5":
        print("Calculator cleared!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)

    elif choice == "2":
        result = subtract(num1, num2)

    elif choice == "3":
        result = multiply(num1, num2)

    elif choice == "4":
        result = divide(num1, num2)

    else:
        print("Invalid choice")
        continue

    print("Result =", result)