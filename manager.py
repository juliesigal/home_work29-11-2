from employee import Employee

class Manager(Employee):
    def __init__(self, id, name, address, age, num_of_emp, emp_rate):
        super().__init__(id,name,address, age)
        self.num_of_emp = num_of_emp
        self.emp_rate = emp_rate

    def calculateSalary(self, num_of_emp, emp_rate):
        return self.num_of_emp * self.emp_rate

    def __str__(self):
        return super().__str__() + f" manage's number of employees is: {self.num_of_emp} " + \
               f"manager's rate per employee is: {self.emp_rate}"
