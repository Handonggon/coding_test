def solution(a, b, n):
    answer = 0
    count = 0
    while n >= a:
        mo = n//a
        answer += mo*b
        na = n%a
        count += na
        n = mo*b + na
    return answer