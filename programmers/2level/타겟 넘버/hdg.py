def solution(numbers, target):
    stack = [[0,0]]
    answer = 0
    l = len(numbers)
    while stack != []:
        a = stack.pop()
        if a[1] == l:
            if a[0] == target:
                answer += 1
        else:
            stack.append([a[0]+numbers[a[1]],a[1]+1])
            stack.append([a[0]-numbers[a[1]],a[1]+1])
        
    
    return answer