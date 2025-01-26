#WAP to create dictionaries for below task and perform all the above operations on it.
my_dict = {
    "id":11,
    "name": "Saniya",
    "age": 20,
    "course": "Data Science"
}
print(my_dict)
# Add a new key-value pair
my_dict["grade"] = "A"

#Update an existing key-value pair
my_dict["age"] = 21

my_dict["Addr"]="kalyan"
print(my_dict)


#find all the keys present in the dictionary
print(my_dict.keys())


#Delete a key-value pair
del my_dict["course"]

#to remove certain element from the dictionary
my_dict.popitem()

print(my_dict)


#Display all keys and values
print("All Keys:", list(my_dict.keys()))
print("All Values:", list(my_dict.values()))
