class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):

            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def info(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Theophilus', 3)
s1.show()

s1.lap.brand = 'hp'
print(s1.lap.brand)
