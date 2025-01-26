'''
ordered:
when we say that tuples are ordered,it means that the items have a defined order,and that will not change.
unchangeables are unchangeable,meaning that we cannot change,add or remove items after the tuple has been created.
since tuples are indexed,they can have items with the same value:
'''
'''thistuple = ("apple","banana","cherry","apple","cheery")
print(thistuple)
#find the length of the tuple
print(len(thistuple))

#tuple is also recognized by its index no.
print(thistuple[0])
print(thistuple[3])
print(thistuple[2:4])'''


tuple1=("aditya",78,"o garde",56000,"navi mumbai")
print(tuple1)

print(type(tuple1))
#slicing a tuple

print(tuple1[1:4])
print(tuple1[2:])
print(tuple1[:5])

#negative indexing
print(tuple1[-2])
print(tuple1[-1])

#note:
#list is a collection which is orederd and changeable.
#list allows duplicate members.
#tuple is a collection which is ordered and unchangeable.
#tuple allows duplicate members.
t1=("aditya",78,"o garde",56000,"navi mumbai")
t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)
