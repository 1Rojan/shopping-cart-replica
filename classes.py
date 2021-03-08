
class Employee:
    raise_salary = 1.4

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @classmethod
    def apply_raise(cls):
        cls.pay = 1.5

emp1 = Employee("Corey", "Schafer", 5000)
print(emp1.raise_salary)
