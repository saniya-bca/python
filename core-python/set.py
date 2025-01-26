'''
set in python programming is an unordered collection data type that is iterable and has no duplicate elements.while sets are mutable,meaning you can add or remove elements after their creation.
'''
set_a={5,8,67,3,6}
print(set_a)

set_b={7,9,5,6}
print(set_b)

set_c={7,8,78,4}
print(set_c)

#set union operation
set_d=set_a.union(set_b)
print("the union of both the sets are:",set_d)

set_e=set_a.union(set_b,set_c)
print("the union of all the sets are:",set_e)


#using union operator |
result=set_a|set_b|set_c
print("the union of all",result)


#WAP to find intersection of two sets using intersection() function
set_f=set_a.intersection(set_b)
print("the intersection of all the sets are:",set_f)

#using intersection operator &
result=set_a & set_b
print("the intersection of all",result)

#set difference between(-)
result=set_a-set_b
print("the difference is:",result)

#set difference using difference()method
result=set_a.difference(set_b)
print("the difference is:",result)


#WAP to get symmetric-difference (elements which are not in both the sets)
result=set_a ^ set_b
print("the symmetric difference is:",result)
