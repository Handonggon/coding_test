def solution(land): #동적 프로그래밍(DP)알고리즘을 참고했습니다.
    land2 = []
    for i in range(len(land)):
        if i == 0:
            land2.append(land[i])
        else:
            list_n = []
            for j in range(4):
                a = land2[i-1].copy()
                a.pop(j)
                list_n.append(land[i][j] + max(a))
            land2.append(list_n)
            
    return max(land2[-1])