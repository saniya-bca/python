#You have a list of employee records,and you need to create a new list that contains the name of employees who work in the 'sales' department,all in uppercase.
#hint:create dictionary with name,department and salary field.

employees = [
    {"name": "riya", "department": "Sales", "salary": 50000},
    {"name": "seema", "department": "Engineering", "salary": 70000},
    {"name": "shreya", "department": "Sales", "salary": 45000},
    {"name": "danish", "department": "Marketing", "salary": 60000},
    {"name": "sahil", "department": "Sales", "salary": 52000},
]
# Create a new list with the names of employees in the 'Sales' department, in uppercase
sales_employees = [employee["name"].upper() for employee in employees if employee["department"].lower() == "sales"]

print(sales_employees)
