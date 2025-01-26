#Each student in a school is associated with their grade.
#Create a dictionary of students with their grades
students = {
    "Saniya": "A",
    "Farheen": "c",
    "Ayman": "B",
    "Shabana": "A"
}
print(students)

#Add a new student with their grade
students["Mishkat"] = "B"
print(students)

#Update the grade of an existing student
students["Farheen"] = "A"
print(students)


#to remove certain element from the dictionary
students.popitem()

print(students)


#to get keys from the dictionary
for i in students.keys():
    print(i)

#to get values from the list
for i in students.values():
    print(i)

