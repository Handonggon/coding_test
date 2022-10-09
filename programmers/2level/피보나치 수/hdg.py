list_n = [0,1]
for i in range(100000):
    list_n.append(list_n[-1] + list_n[-2])
def solution(n):
    answer = list_n[n]%1234567
    return answer