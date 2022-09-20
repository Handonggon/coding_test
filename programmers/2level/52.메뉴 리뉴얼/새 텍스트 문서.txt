from itertools import *
def solution(orders, course):
    dict = {}
    answer = []
    combinations('ABCD', 2)
    return answer
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
함수형 프로그래밍? 
from itertools import *
def manual_cre(menu,manual,k): #메뉴얼 만드는 함수
    for i in list(combinations(menu, k)):
        a = ""
        for j in i:
            a += str(j)
        manual[a] = 0 
def manual_reg(menu,manual,k): #판매메뉴 정리하는 함수
    for i in list(combinations(menu, k)):
        a = ""
        for j in i:
            a += str(j)
        manual[a] += 1
def solution(orders, course):
    manual = {}
    answer = []
    for i in orders: #메뉴얼 만들기
        for j in course:
            manual_cre(i,manual,j)
    
    for i in orders: #판매메뉴 정리
        for j in course:
            manual_reg(i,manual,j)

    dict = {}
    for i in course:
        dict[str(i)] = []


    for i in manual:
        a = len(i)
        for j in course:
            if a == j:
                dict[str(a)].append()
    
    
    

    
    

    return manual
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

from itertools import *
def manual_cre(menu,manual,k): #메뉴얼 만드는 함수
    for i in list(combinations(menu, k)):
        i = sorted(i)
        a = ""
        for j in i:
            a += str(j)
        manual[a] = 0 
def manual_reg(menu,manual,k): #판매메뉴 정리하는 함수
    for i in list(combinations(menu, k)):
        i = sorted(i)
        a = ""
        for j in i:
            a += str(j)
        manual[a] += 1
def solution(orders, course):
    manual = {}
    answer = []
    for i in orders: #메뉴얼 만들기
        for j in course:
            manual_cre(i,manual,j)
    
    for i in orders: #판매메뉴 정리
        for j in course:
            manual_reg(i,manual,j)

    dict = {}
    for i in course:
        dict[str(i)] = []




    for i in manual:
        a = len(i)
        for j in course:
            if a == j:
                dict[str(a)].append([i,manual[i]])

    for i in dict:
        dict[i] = sorted(dict[i],key = lambda x : x[1])
    
    
    for i in dict:
        if len(dict[i]) > 0:
            if dict[i][-1][1] > 1:
                a = dict[i].pop()
                answer.append(a[0])
            else:
                continue

            while dict[i][-1][1] == a[1]:
                a = dict[i].pop()
                answer.append(a[0])
        else:
            pass
                
    answer.sort()

    
    

    return answer
    