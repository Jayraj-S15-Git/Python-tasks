# static methods & class methods


class Employee:
    comName = "microsoft"

    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
        
    @classmethod
    def changeCompany(cls, newCompany):
        cls.comName = newCompany
    @staticmethod
    def show():
        print(f"This is method show of Employee")

rakesh =  Employee(102, 45000)
Employee.show()

Employee.changeCompany("Google")
rakesh = Employee(102, 45000)
print(rakesh.comName)  # prints Google

raju = Employee(105, 30000)
print(raju.comName)  # prints Google
