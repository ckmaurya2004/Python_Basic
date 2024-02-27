class Employee():
    no_of_leaves = 8
    
    def __init__(self,aname,myage,arole):
        self.name = aname
        self.age = myage
        self.role = arole

    def printdetail(self):
        return f"name is {self.name} and age is {self.age} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leave):
        cls.no_of_leaves = new_leave
       


kiran = Employee("kiran",19,"programmer")  
 


print(kiran.role)
print(kiran.printdetail())
kiran.change_leaves(7)
print(kiran.no_of_leaves)

# print(kiran.__dict__)
# print(Employee.__dict__)