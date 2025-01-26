#WAP to check whether person can vote or not using function.

def vote(age):
    """Function to check if a person can vote."""
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

#Input from the user
age = int(input("Enter your age: "))

#Calling the function and displaying the result
result = vote(age)
print(result)
