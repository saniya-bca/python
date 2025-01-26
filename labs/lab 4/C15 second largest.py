#WAP to find second largest number in a list

l2=[90,47,54,65,89,68]

remove_dup=(list(set(l2)))
print("The final list is",remove_dup)

sorted_list=sorted(remove_dup)
print(sorted_list)

print("The second largest element is:",sorted_list[-2])
