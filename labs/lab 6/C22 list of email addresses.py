#You have a list of email addresses and you want to extract the domain part (the part
#after '@') from each email address.
# List of email addresses
emails = ["seema1@gmail.com", "riya.user@yahoo.com", "info@company.org"]

# Extract domains using list comprehension
domains = [email.split("@")[1] for email in emails]

print(domains)
