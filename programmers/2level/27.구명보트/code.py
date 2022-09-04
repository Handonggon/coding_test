from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    island = deque([])
    for i in people:
        island.append(i)
    while island != deque([]):
        boat = []
        answer += 1
        if len(island) > 1:
            a = island.pop()
            b = island.popleft()
            boat.append(a)
            if a + b <= limit:
                boat.append(b)
            else:
                island.appendleft(b)
        else:
            island.pop()
        
                
    
    
    return answer