'''A dictionary is a built-in data structure in python that allows you to store a collection of key-value pairs.
dictionary is mutable and it is unordered'''
my_dict={
    "std_id":123,
    "std_name":"sameera",
    "course":"BCA"
}
print(my_dict)

x=my_dict["course"]
print("The course selected is:",x)

x=my_dict.get("std_id")
print(x)

#find all the keys present in the dictionary
print(my_dict.keys())
#print("The keys present are:",y)

#to update dictionary element

my_dict.update({"std name":"sameer"})
print(my_dict)
#to add new element in the dictionary
my_dict["fees"]=76000
print(my_dict)

my_dict["std_Addr"]="navi mumbai"
print(my_dict)

#to remove certain element from the dictionary
my_dict.popitem()

print(my_dict)

#looping over dictionary

for i in my_dict:
    print(i)

#to get keys from the dictionary
for i in my_dict.keys():
    print(i)

#to get values from the list
for i in my_dict.values():
    print(i)

for x,y in my_dict.items():
    print(x,y)
