# from itertools import *
# def solution(nums):
#     answer = 0
#     list_b = list(set(list(combinations(nums,int(len(nums)/2)))))
#     jr = []
#     for i in list_b:
#         jr.append(len(set(i)))
#     answer = max(jr)
    
#     return answer
##시간초과

from itertools import *
def solution(nums):
    list_b = list(set(nums))
    a = len(list_b)
    b = int(len(nums)/2)
    if a <= b :
        answer = a
    else :
        answer = b
    return answer