# Build a Calculator CLI App
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b
def display_menu():
    """Display calculator menu options."""
    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
def main():
    """Main function to run calculator."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                print("Result:", result)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")
if __name__ == '__main__':
    main()
# This file contains the code for a Command Line Interface calculator app.
