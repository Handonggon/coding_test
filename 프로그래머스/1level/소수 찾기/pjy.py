def solution(n):
    list_n = list(range(n+1))
    for i in list_n:
        if i < 2:
            list_n[i] = 0
        else:
            for j in range(i,n+1,i):
                list_n[j] = 0
            list_n[i] = i
    while 0 in list_n :
        list_n.remove(0)


    
    return len(list_n)
=> 시간초과

def solution(n):
    answer = []
    list_n = list(range(n+1))
    for i in range(len(list_n)):
        if i < 2:
            list_n[i] = 0
        else:
            if list_n[i] != 0:
                for j in range(i,n+1,i):
                    if list_n[j] != 0:
                        list_n[j] = 0
                answer.append(i)

    return len(answer)

=> while문 안쓰는방법 성공