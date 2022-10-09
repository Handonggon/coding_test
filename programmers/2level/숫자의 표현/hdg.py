def solution(n):
    answer=1
    list_n = []
    if n == 1:
        return 1
    if n == 2:
        return 1
    for i in range(1,(n//2)+2):
        list_n.append(i)
        if sum(list_n) ==n:
            answer+=1
        elif sum(list_n) > n:
            while sum(list_n) > n:
                list_n.pop(0)
                if sum(list_n)==n:
                    answer+=1
                    break
                else:
                    pass
        else:
            continue
            
    return answer