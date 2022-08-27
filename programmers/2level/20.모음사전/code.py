from itertools import *
keyword = 'AEIOU'
a = list(product(keyword, repeat=1))
b = list(product(keyword, repeat=2))
c = list(product(keyword, repeat=3))
d = list(product(keyword, repeat=4))
e = list(product(keyword, repeat=5))

dict = []
for i in a:
    m = ""
    for j in i:
        m += j
    dict.append(m)
for i in b:
    m = ""
    for j in i:
        m += j
    dict.append(m)
for i in c:
    m = ""
    for j in i:
        m += j
    dict.append(m)
for i in d:
    m = ""
    for j in i:
        m += j
    dict.append(m)
for i in e:
    m = ""
    for j in i:
        m += j
    dict.append(m)
dict.sort()
def solution(word):
    for i in range(len(dict)):
        if dict[i] == word:
            return i+1