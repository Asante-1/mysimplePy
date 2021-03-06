
'''def recur(array):

    data = { }

    for i in array:
        data[i] = data.get(i, 0) + 1
        if data.get(i, 0) > 1:
            return i
    return None

print(recur([5,5,3,1,2,2,2]))'''


'''def average(array):
    # your code goes here
    av = sum(array)/len(array)
    




n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)'''

'''
from collections import defaultdict

d = defaultdict(lambda : "None")
d['python'] = 'awesome'
d['something-else'] = 'not relevant'
d['python'] = 'language'

print(d.items())
print(d['banku'])
'''


'''#calendar
import calendar
mdy = input().split()
mm = int(mdy[0])
dd = int(mdy[1])
yyyy = int(mdy[2])

c = calendar.weekday(yyyy, mm, dd)

if c == 0:
    print('MONDAY')
elif c == 1:
    print('TUESDAY')
elif c == 2:
    print('WEDNESDAY')
elif c == 3:
    print('THURSDAY')
elif c == 4:
    print('FRIDAY')
elif c == 5:
    print('SATURDAY')
elif c == 6:
    print('SUNDAY')
'''

# def fib(n):
#     net = []
#     a = 0
#     b = 1
#
#     if n == 1:
#         return [1]
#     elif n == 0:
#         return []
#     else:
#         net.append(a)
#         net.append(b)
#
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             net.append(c)
#             return net
#
# print(fib(5))
# # num = list(map(lambda x: x ** 3, fib(4)))
# # print(num)



from collections import namedtuple, deque

# a = namedtuple('Student', 'Name, CWA')
#
# student1 = a('Theophilus Asante', 71.33)
# student2 = a('Michael Adiyah', 66.90)
# print(student1.Name,'\n')
# print(student2)
#
# d = ['w', 'e', 'f']
# d = deque(d)
# d.appendleft('python')
# print(d)

# def break_all():
#     for j in range(1, 5):
#         for i in range(1,4):
#             if i*j == 6:
#                 return(i)
#             print(i*j)
# break_all()




# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'Theo']
#
# for s in lst[1::2]:
#     print(s)

'''
import datetime
class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height
    def __repr__(self):
        return self.name
l = [Person("John Cena", datetime.date(1992, 9, 12), 175),
Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

l.sort(key=lambda item: item.name)
'''

'''
sentence = "Beautiful is better than ugly"
now = ["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
print(now)
'''






