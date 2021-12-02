from employee import Employee
class Worker(Employee):
    def __init__(self, id, name, address, age, hours_per_day, hour_rate):
        super().__init__(id,name,address, age)
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate

    def calculateSalary(self, hours_per_day, hour_rate):
        return self.hours_per_day * self.hour_rate

    def __str__(self):
        return super().__str__() + f" worker's hours per day is: {self.hours_per_day} "  + \
               f"worker's rate per hours is: {self.hour_rate}"
