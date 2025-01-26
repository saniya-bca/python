#WAP to get table of a number using function.

def table(number):
    """Function to print the multiplication table of a number."""
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input from the user
num = int(input("Enter a number to get its multiplication table: "))

# Calling the function to print the table
table(num)
