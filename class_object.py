class Employee():
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"The name is {self.name}.Salary is {self.salary} and {self.role}"


# kiran = Employee()
# ruchi = Employee()
shikha = Employee("kiran",19000,17)

# kiran.name = "Kiran Maurya"
# kiran.salary = 100
# kiran.role = 18


# ruchi.name = "Ruchi Maurya"
# ruchi.salary = 1000
# ruchi.roll = 17

# print(kiran.name)
# print(kiran.salary)
# print(kiran.roll)

# print(ruchi.name)
# print(ruchi.salary)
# print(ruchi.roll)

print(shikha.printdetail())
# print(kiran.printdetail())
