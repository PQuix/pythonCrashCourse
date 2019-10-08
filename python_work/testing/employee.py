from employee_class import Employee

new_employee = Employee('tom', 'gundersen', '400000')

print("The employee's name is " + new_employee.get_full_name())

increase = '80000'

print(new_employee.get_full_name() + " was given a raise of " + increase + ".")

new_employee.give_raise(increase)
print("Their new salary is " + str(new_employee.get_salary()) + ".")

