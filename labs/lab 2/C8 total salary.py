#To accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.
salary = int(input("Enter the basic salary: "))

if salary > 50000:
    da = 10 * salary   # 10% DA
    hra = 12 * salary  # 12% HRA
else:
    da = 0
    hra = 0

total_salary = salary + da + hra
print("The total salary is:", total_salary)
