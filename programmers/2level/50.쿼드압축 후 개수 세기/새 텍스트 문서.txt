# def solution(arr):
#     answer = []
#     return answer
arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
n = len(arr)
quad = n

a = 0
b = 2
c = 2
d = 4
box = [i[c:d] for i in arr[a:b]]
