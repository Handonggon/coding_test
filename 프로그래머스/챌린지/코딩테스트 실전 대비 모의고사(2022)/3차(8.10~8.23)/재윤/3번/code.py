def solution(distance, scope, times):
    answer = 0
    dis = [0 for i in range(distance+1)]
    for i in scope:
        i.sort()
    for i in range(len(scope)):
        dis[scope[i][0]:scope[i][1]+1] = [times[i] for j in range(scope[i][0],scope[i][1]+1)]
    while answer != distance:
        answer += 1
        if dis[answer] == 0:
            pass
        else: #[0, 0, 0, [2, 5], [2, 5], [4, 3], [4, 3], [4, 3], [4, 3], 0]
            if answer%(dis[answer][0]+dis[answer][1])>dis[answer][0] or answer%(dis[answer][0]+dis[answer][1])== 0 :
                pass
            else:
                return answer
    return answer
            
