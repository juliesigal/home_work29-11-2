1. לא ניתן ליצור מופע ממחלקה אבסטרקטית, אלא ממחלקת ירושה שלא אבסטרקטית
2. כדאי להגדיר את המחלקה כאבססטרקטית, כאשר יש כמה מחלקות ובה הבסיס המשותף לכל מחלקות היורשות.
3. כדאי להגדיר פונקציה כאבסטרקטית, כאשר אנחנו לא רוצים שידלגו עליה במחלקות.
4 כן, אם זו פונקציה הכרחית למחלקה שיכולים בטעות או לא בטעות לדלג עלליה.
5. כדאי להשתמש בפונקצית סופר כדי להמנע מלחזור על אותה הפעולה של יצירת אותן שדות נתונים שכבר נוצרו במחלקה האבסטרקטית.
6. כדאי להשתמש בפונקצית סופר כדי להמנע מלחזור על אותה הפעולה של הצבה בהדפסה של המחלקה

7: 
  from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, id,name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    def calculateSalary(self):
        @abstractmethod
        pass

    def __str__(self):
        return f'[Employee] id: {self.id},name: {self.name}, address: {self.address}, age: {self.age}'

class Worker(Employee):
    def __init__(self, id, name, address, age, hours_per_day, hour_rate):
        super().__init__()
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate

    def calculateSalary(self, hours_per_day, hour_rate):
        return self.hours_per_day * self.hour_rate

    def __str__(self):
        return super().__str__() + f"worker's hours per day is: {self.hours_per_day} " +
               f"worker's rate per hours is: {self.hour_rate}"

   class Kablan(Employee):
    def __init__(self, id, name, address, age, num_project, project_rate):
        super().__init__()
        self.num_project = num_project
        self.project_rate = project_rate

    def calculateSalary(self, num_project, project_rate):
        return self.num_project * self.project_rate

    def __str__(self):
        return super().__str__() + f"kablan's numbers of projecs is: {self.num_project} " +
        f"kablan's rate per project is: {self.project_rate}"     
