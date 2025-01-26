#Each customer ID in a company is associated with a customer name.
#Create a dictionary of customer IDs and names
customers = {
    101: "David Clark",
    102: "Anthony King",
    103: "vijay sharma",
    104: "Sameer khan"
}

print(customers)

#Add a new customer
customers[105] = "Riya sharma"
print("Added customer ID 105: 'Riya sharma'.")

#Update an existing customer's name
customers[102] = "Robert Smith"
print("\nUpdated customer ID 102 to 'Robert Smith'.")

#to remove certain element from the dictionary
customers.popitem()

print(customers)


#to get keys from the dictionary
for i in customers.keys():
    print(i)

#to get values from the list
for i in customers.values():
    print(i)
