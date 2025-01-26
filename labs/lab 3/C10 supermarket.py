#Each product in a supermarket is associated with its price.
#Create a dictionary of products with their prices
supermarket = {
    "Apples": 253,
    "Bananas": 105,
    "Carrots": 211,
    "Tomato": 464
}
print(supermarket)


#Add a new product
supermarket["Eggs"] = 236
print("Added 'Eggs' to the supermarket.")
print(supermarket)

#Update the price of an existing product
supermarket["Bananas"] = 105
print("\nUpdated price of 'Bananas'.")
print(supermarket)

#to remove certain element from the dictionary
supermarket.popitem()

print(supermarket)


#to get keys from the dictionary
for i in supermarket.keys():
    print(i)

#to get values from the list
for i in supermarket.values():
    print(i)

