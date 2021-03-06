marksheet = []
scoresheet = []

for i in range(int(input("Enter number of students"))):
    name = input("Enter name of student.")
    score = float(input("Enter score of the indicated student"))
    marksheet += [[name, score]]
    scoresheet += [score]

x = sorted(set(scoresheet))[1]


for name, score in marksheet:
    if score == x:
        print(name)


