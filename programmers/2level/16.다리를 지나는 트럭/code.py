def solution(length, mw, truck):
    answer = 0
    bridge = []
    truck.reverse()
    a = truck.pop()
    bridge.append([a,0])
    while bridge != []:
        answer += 1
        for i in bridge:
            i[1] += 1
        while bridge[0][1] == length:
            bridge = bridge[1:]
        if sum(bridge)+a >= mw:
            bridge.append([a,0])
        
    
    return answer