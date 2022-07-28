def solution(n):
    answer = ''
    while n > 0:
        answer = "412"[n%3] + answer
        n = n//3 - (n%3==0)
    return answer