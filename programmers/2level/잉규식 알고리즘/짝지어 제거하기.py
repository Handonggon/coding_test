def solution(s):
    stack = [0]
    for i in s :
        if stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    
    if stack == [0] :
        return 1
    else :
        return 0