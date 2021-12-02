from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, id,name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    @abstractmethod
    def calculateSalary(self):
        pass

    def __str__(self):
        return f'[Employee] id: {self.id},name: {self.name}, address: {self.address}, age: {self.age}'

