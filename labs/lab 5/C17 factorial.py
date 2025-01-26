#WAP to get factorial of a number using function.

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

#Input from the user
number = int(input("Enter a number to find its factorial: "))

#Calling the function and displaying the result
print(f"The factorial of number is: {factorial(number)}")
