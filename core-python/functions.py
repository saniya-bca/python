#function is self contained block of statement which has specific task to perform
#same block of code can be reused whenever required.
'''def myfunction():
    print("hello all to the world of struggle")
myfunction()

def add(a,b):
    c=a+b
    print("the addition is",c)

a=int(input("enter first number"))
b=int(input("enter second number"))
add(a,b)

#WAP to get area of rectangle
def myfunction(l,b):
      area=l*b
      print("the area of rectangle is:",area)
l=int(input("enter first number"))
b=int(input("enter second number"))
myfunction(l,b)
#WAP to get area of circle

def myfunction(r):
      area=3.14*r*r
      print("the area of circle is:",area)
r=int(input("enter number"))

myfunction(r)

#WAP to remove duplicate from the list
def remove_duplicates(lst):
    print(list(set(lst)))
lst=[76,89,45,45,76,90]

remove_duplicates(lst)

#when to use return
def rem_dup(l2):
    return list(set(12))

l2=[78,67,89,67,67]
ans=rem_dup(12)
print("the clean data set is:",ans)'''
#WAP to calculate the factorial of a number.
#using recursion function calling itself again and again
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("enter a number"))
ans=factorial(n)
print("factorial of",n,"is",ans)

