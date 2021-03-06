'''s = input()
#string validators
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
'''

'''
#capitalize hackerrank
import string

def solve(s):
    #return ' '.join(i.capitalize() for i in s.split(' '))
    return string.capwords(s, ' ')
    # have to return it on one line or you can use capwords module

s = input()
result = solve(s)
print(result)
'''

'''
# merge repeated string
import textwrap

def merge_repeatedstring(string, k):
    l = textwrap.wrap(string, k)


    for i in range(len(string)//k):
        mylist = list(dict.fromkeys(l[i]))
        print(''.join(mylist))



string = input()
k = input()
merge_repeatedstring(string, k)

'''


'''
from itertools import combinations_with_replacement
def possibe_com(string, num):
    x = (list(combinations_with_replacement(string, num)))
    for i in range(len(x)):
        print(x[i])



string_num = input().split()
string = string_num[0]
num = string_num[1]
number = int(num)
possibe_com(string, number)
'''

"""
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

pc = list(product(A,B))
for elem in pc:
    print(elem, end=' ')

"""

"""
from itertools import combinations_with_replacement

line = input().split()
word = line[0]
print(word)
word = list(word)
print(word)
word.sort()
print(word)
word = "".join(word)
print(word)

n = int(line[1])

li = list(combinations_with_replacement(word, n))
for i in li:
     print("".join(list(i)))
"""

'''from itertools import permutations

line = input().split()

word = line[0]
word = list(word)


num = int(line[1])

li =list(permutations(word, num))
for i in li:
    print("".join(i))'''