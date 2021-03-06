# Gives the name, salary and occupation of an emplotee
class Employee:
    empcount = 0
    def __init__(self, name, salary, occupation):
        self.name = name
        self.salary = salary
        self.occupation = occupation
        Employee.empcount += 1

    def Employeeinfo(self):
        print('Name: ' + str(self.name))
        print('Salary :' + str(self.salary) )
        print('Occupation: ' + str(self.occupation) + '\n')



emp1 = Employee('Ansah Boakye Kwabena', 5000, 'Programmer')
emp2 = Employee('Asante Theophilus Asante', 6600, 'Programmer')
emp3 = Employee('Atiase Gloria Xorlali', 3500, 'Secretary')
emp1.Employeeinfo()
emp2.Employeeinfo()
emp3.Employeeinfo()


print('Total employees are ', Employee.empcount,'.' )



