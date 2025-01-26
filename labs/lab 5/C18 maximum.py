#WAP to find maximum among two number.

def find_maximum(a, b):
    """Function to find the maximum of two numbers."""
    if a > b:
        return a
    else:
        return b

#Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Calling the function and displaying the result
maximum = find_maximum(num1, num2)
print(f"The maximum number  is: {maximum}")

