from abc import ABC, abstractmethod
from employee import Employee
from worker import Worker
from manager import Manager
from kablan import Kablan


work1 = Worker(1, 'John', 'israel', 28, 8, 30)
man1 = Manager(2, 'Din', 'Dubai', 35, 4, 1000)
kab1 = Kablan(3, 'Dave', 'USA', 45, 5, 1500)
print(work1)
print(man1)
print(kab1)