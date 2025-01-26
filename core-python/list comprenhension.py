'''
to present list in concise and easy way we use list comprehension.as size of the code is less,performance will be increased.'''
marks =[20,35,50,78,40]
new_marks=[]
for x in marks:
    new_marks.append(x+2)
print(new_marks)

#code using list comprehension
marks=[20,35,50,78,40]
new_marks=[x+2 for x in marks]
print(new_marks)

'''Q.2) find cube of even numbers'''
cubes=[]
for x in range(11):
    if x%2==0:
        cubes.append(x**3)
print("listing for loops",cubes)
#using list comprehension
easy=[x**3 for x in range(10) if x%2==0]
print("using list comprehension",easy)

#using set comprehension
easy={a**3 for a in range(10) if a%2==0}
print("using set comprehension",easy)


