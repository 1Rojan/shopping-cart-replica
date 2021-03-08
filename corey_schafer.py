# class Employee:
#     no_of_employee = 0
#     raise_amount = 1.2
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = self.first + self.last + '@gmail.com'
#         Employee.no_of_employee += 1
#
#     def full_name(self):
#         return self.first + ' ' + self.last
#
#     def apply_raise(self):
#         self.pay = self.pay * self.raise_amount
#         return self.pay
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp):
#         fname, lname, pay = emp.split('-')
#         return(cls(fname, lname,pay))
#
# class Developer(Employee):
#     pass
#
# emp_obj = Developer('corey', 'schafer', 5000)
# print(emp_obj.full_name())
# print(emp_obj.apply_raise())
#
# Employee.set_raise_amount(1.5)
#
# print(Employee.raise_amount)
# print(emp_obj.raise_amount)
#
#
# emp1 = "rojan-sunar-2000"
#
# new_emp =Employee.from_string(emp1)
# print(new_emp.first)


# ----closure----

def outer():
    message = "Hi"
    def inner():
        print(message)
    return inner

a = outer()
print(a.__name__)