#List is a collection which is ordered and changeable.
#allow duplicate members.

my_list=["Soap","oil","maggie",345,"rice","tea","buiscuits",]
print(my_list)

for i in my_list:
    print(i)
my_list.append("dalia")
print(my_list)

#list element is recognized by its index value
#list element my_list[0]

print(my_list[0])


#there is concept of negative indecxing.
print(my_list[-1])

#slicing
print(my_list[1:4])
print(my_list[:])
print(my_list[2:])
print(my_list[:5])
print(my_list[::-1])
