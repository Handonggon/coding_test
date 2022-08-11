def solution(priorities, location):
    a = [False for _ in range(len(priorities))]
    a[location] = True
    res = 1
    
    while True:
        if priorities:
            b = max(priorities)
            d = priorities.pop(0)
            c = a.pop(0)
            if b == d and c == False:
                res +=1
            elif b==d and c == True:
                return res
            else:
                priorities.append(d)
                a.append(c)