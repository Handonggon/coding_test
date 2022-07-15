def solution(x, n):
    # answer = []
    # if x == 0:
    #     answer = [0 for i in range(n)]
    # else:
    for i in range(x,(x*n)+int((x/abs(x)),x)): #괄호를 잘못감음
        answer.append(i)
    return answer


def solution(x, n):
    answer = []
    if x == 0:
        for i in range(n):
            answer.append(0)
            continue
    else:
        for i in range(x,(x*n)+int(x/abs(x)),x):
            answer.append(i)
    return answer

