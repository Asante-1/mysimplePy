studentsheet = {}
num = int(input("enter the number of students:"))
for i in range(num):
    name, *m = input().split( )
    mark = list(map(float, m))
    studentsheet[name] = mark


query_name = input("Enter the name to calculate your percentage:")

for name, mark in studentsheet.items():
    if query_name == name:
        print("Your average is: {0:.2f}".format(sum(studentsheet[name])/len(mark)))











    """for k , v in studentsheet.items():
        studentsheet[k] = name
        studentsheet[v] = marks
        print(studentsheet)"""
