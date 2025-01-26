#1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.

#Create an empty list
dynamic_list = []

#Ask the user to enter 5 elements
print("Enter 5 elements to create the list:")
for i in range(5):
    element = input("Enter element:")
    dynamic_list.append(element)

#Insert a new element
new_element = input("\nEnter a new element to insert into the list:")


#Delete an element
element_to_delete = input("\nEnter an element to delete from the list:")


#Final list display
print("\nFinal list:", dynamic_list)
