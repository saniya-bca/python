#1)A string represents a sequence of characters.
#2)It is an immutable data type in most of the programming languages including java and python,meaning that once you have created a string, you cannot change it.
#3)Python programming does not have a character data type,a single character is simply a string with a length of 1.
#4)String in python can be created using single quotes or double quotes or even triple quotes.
#5)In this example,we will demonstrate different ways to create a python string.
#6)We will create a string using single quotes(' '),double quotes(" "),
#and triple quotes(""" """).the triple quotes can be used to declare multiline strings in python.

'''str1=input("enter your name")
str2=input("enter last name")
print(str1[0])
print(str1[-1])

#slicing
print(str1[1:6])

#concatination
res=str1+str2
print("the concatinated string is",res)

#repetition (*):
#the  * operator allows you to repeat a string a specified number of times.

ans=str1*4
print("the expected answer is",ans)'''

'''#methods related to string
text="helloworld"
text_upper=text.upper()
print("the data in uppercase is",text_upper)

text_lower=text.lower()
print("the data in lowercase is",text_lower)

name="  sam  "
newname=name.strip()
print("the data without space is",newname)
rspace=name.rstrip()
print("the data without space is",rspace)
lspace=name.lstrip()
print("the data without space is",lspace)'''

#str.replace(old,new): this method replace all occurrences of the "old" substring
#with the "new" substring in the string.

sentence = " I like apples,and i like pineapple."
new_sentence = sentence.replace("like","love")
print(new_sentence)



