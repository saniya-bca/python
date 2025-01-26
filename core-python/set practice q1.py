'''sports1={"sanoj","Neha","Dev","Raj","Shweta","Hirai"}
sports2={"Neha","Shweta","Hirai","Arjun","Ram","Sejal"}
#Find total participants in the sports list
Total_Ath=sports1|sports2
print("Total participants:",Total_Ath)
for s in Total_Ath:
    print(s)
#Set difference
New_sports1=sports1-sports2
print("The new sports one list is:",New_sports1)'''

#WAP to accept different email ids of customer at least 3) in list and try to print unique emails 
emails_data=["abc12@gmail.com","xyz213@gmail.com","qwe342@gmail.com","abc12@gmail.com","qwe342@gmail.com"]
print("the data of email as below:")
print(emails_data)

unique_emails=set(emails_data)
print("The unique data is:",unique_emails)

new_emails={"raj@gmail.com","Harsh@gmail.com","sang@gmail.com","Rax1@gmail.com"}
update=new_emails-unique_emails
print("New customers are:",update)


