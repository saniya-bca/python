#WAP to reverse a given number for example n=123 rev=321

n=int(input("Enter a number"))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("the reverse of a  given number",rev)


