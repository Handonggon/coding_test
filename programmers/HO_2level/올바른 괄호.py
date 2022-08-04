def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []:
                return False
            stack.pop()
            
    if len(stack) >= 1:
        return False
    return True 