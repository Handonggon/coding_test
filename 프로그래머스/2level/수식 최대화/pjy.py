from collections import deque
from itertools import *
def operation(list_w,op): #주어진 연산자로 계산하는 함수
    if len(list_w) == 1:
        return list_w

    answer = deque([])
    while len(list_w) > 1:
        if len(answer) > 0:
            a = answer.pop()
        else:
            a = list_w.popleft()
        b = list_w.popleft()
        c = list_w.popleft()
        if b == op:
            if op == "+":
                d = str(int(a) + int (c))   
            elif op == "-":
                d = str(int(a) - int (c))
            elif op == "*":
                d = str(int(a) * int (c))
            answer.append(d)
        else:
            answer.append(a)
            answer.append(b)
            answer.append(c)
        
    return answer


def operation_order(expression,f,s,t): #주어진 연산자의 순서대로 계산해서 값을 내뱉는 함수
    list_w = deque([])
    a = ''
    for i in expression:
        if i.isdigit() == True:
            a += i
        else:
            list_w.append(a)
            list_w.append(i)
            a = ""
    list_w.append(a)

    #퍼스트
    list_w = operation(list_w,f)

    #세컨드
    list_w = operation(list_w,s)

    #서드
    list_w = operation(list_w,t)
    
    return list_w[0]

def solution(expression):
    answer = []
    for i in list(permutations('+-*',3)):
        f = i[0]
        s = i[1]
        t = i[2]
        a = operation_order(expression,f,s,t)
        if int(a) >= 0:
            answer.append(int(a))
        else:
            answer.append(int(a[1:]))
            
    return max(answer)