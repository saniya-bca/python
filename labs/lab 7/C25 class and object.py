#Using class n object concept create basic calculator in python
class Calculator:
    # Constructor
    def __init__(self):
        print("Welcome to the Basic Calculator!")

    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def subtract(self, a, b):
        return a - b

    # Multiplication
    def multiply(self, a, b):
        return a * b

    # Division
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

# Main program
if __name__ == "__main__":
    # Create an object of the Calculator class
    calc = Calculator()

    while True:
        print("\nSelect Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting Calculator. Goodbye!")
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"The result is: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {calc.divide(num1, num2)}")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid number. Please enter numeric values.")

