def solution(n, left, right):
    a = (left//n) + 1 # 2번쨰줄
    b = (right//n) + 1 # 4번쨰줄
    repeat = b-a+1 # 3행 만들기
    list_n = []
    c = (n*(a-1))
    for i in range(repeat):
        for j in range(a):
            list_n.append(a)
        for m in range(a+1,n+1):
            list_n.append(m)
        a += 1
    return list_n[left-c:right-c+1]