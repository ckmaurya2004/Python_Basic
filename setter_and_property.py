class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
       # self.email = f"{self.fname}{self.lname}@gmail.com"

    def printDetail(self):
        return f"The name is {self.fname}and {self.lname} and email is {self.email}"

    @property
    def email(self):
        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        name = string.split('@')[0
        ]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]



kiran=Employee('kiran','maurya')
print(kiran.email)
kiran.fname = "prita"
print(kiran.email)
kiran.email = "this.that@gmail.com"
print(kiran.fname)