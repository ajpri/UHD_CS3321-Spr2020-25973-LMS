from allclasses import Employee, Faculty

def bonus(obj):
    print("Employee Bonus is : ",obj.calculate_bonus())

fname = input("Enter the customer first name :")
lname = input("Enter the customer last name :")
email = input("Enter the customer email :")
dept = input("Enter the Department :")
sp = input("Enter the Specialization :")

faculty1 = Faculty(fname,lname)
faculty1.set_emp_salary(100000)
faculty1.set_emp_id()
faculty1.set_department(dept)
faculty1.set_specialization(sp)
bonus(faculty1)

employee1 = Employee(fname,lname)
employee1.set_emp_id()
employee1.set_emp_salary(50000)
bonus(employee1)




