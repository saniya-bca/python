'''#list comprehension

squares=[x**2 for x in range(1,25) if x%2==0]
print(squares)

#find first letter in given list.
words=["Apple","Banana","Cherry","Date"]
first_letter=[x[0] for x in words]
print(first_letter)

users=[
{"name":"alice","email":"alice@example.com","active":True},
{"name":"bob","email":"bob@example.com","active":False},
{"name":"charlie","email":"charlie@example.com","active":True},
]

#task get the email addresses of active users.
active_email=[x['email'] for x in users if x['active']]
print(active_email)

#lab1
Q.1you have a list of employee records,and you need to create a new list that contains the name of employees who work in the 'sales' department,all in uppercase.
hint:create dictionary with name,department and salary field
Q.2)you have a list of email addresses and you want to extract the domain part (the after '@') from each email addresses.
Q.3) Create list of urls and you need to filter out those that starts with 'https'.
for example:
urls=[
"http://example.com",
"https://secure-site.com",
"ftp://files.example.org",
"https://another-secure-site.com"
]'''

# List of employee records
employees = [
    {"name": "Riya", "department": "Sales", "salary": 50000},
    {"name": "Seema", "department": "Engineering", "salary": 70000},
    {"name": "Shreya", "department": "Sales", "salary": 45000},
    {"name": "Danish", "department": "Marketing", "salary": 60000},
    {"name": "Sahil", "department": "Sales", "salary": 52000},
]

# Create a new list with the names of employees in the 'Sales' department, in uppercase
sales_employees_uppercase = [employee["name"].upper() for employee in employees if employee["department"].lower() == "sales"]

print(sales_employees_uppercase)
# List of email addresses
email_addresses = [
    "alice@example.com",
    "bob@gmail.com",
    "charlie@yahoo.com",
    "diana@outlook.com",
    "eve@company.org"
]

# Extract the domain part from each email address
domains = [email.split("@")[1] for email in email_addresses]

print(domains)

# List of URLs
urls = [
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

# Filter out URLs that start with 'https'
https_urls = [url for url in urls if url.startswith("https")]

print(https_urls)


