from employee import Employee

class Kablan(Employee):
    def __init__(self, id, name, address, age, num_project, project_rate):
        super().__init__(id,name,address, age)
        self.num_project = num_project
        self.project_rate = project_rate

    def calculateSalary(self, num_project, project_rate):
        return self.num_project * self.project_rate

    def __str__(self):
        return super().__str__() + f" kablan's numbers of projecs is: {self.num_project} " + \
        f"kablan's rate per project is: {self.project_rate}"