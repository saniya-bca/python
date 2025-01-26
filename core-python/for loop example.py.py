'''#WAP  to get table of a number
num=int(input("enter a number"))

for i in range(1,11):
    ans=num*i
    print(ans)'''
'''#WAP to generate squares between 10 and 20

for i in range(10,21):
    square=i*i
    print(square)'''
'''#WAP to generate even numbers between 1 and 20
for i in range(1,21):
    if i%2==0:
      print(i)'''
'''st=int(input("enter start value"))
end=int(input("enter end value"))
for i in range(st,end+1):
    if i%2==0:
      print(i)'''

'''#WAP to sum first 10 natural numbers
sum1=0
for i in range(1,11):
 sum1=sum1+i
 print(sum1)
print("the sum of first 10 natural number is",sum1)'''

'''#WAP to find factorial of a number
#5!=5*4*3*2*1=120
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print("factorial of",n,"is",fact)'''

'''#USE of break statement
for i in range(1,25):
    if(i==15):
        break
    print("hello",i)
print("loop exited")'''

#use of continue
for i in range(1,21):
    if(i==10):
        print("skipped")
        continue
print(i)


