def stack_F(s) :
    stack = [0]
    for i in s :
        if i == "]" :
            if stack[-1] == "[" :
                stack.pop()
            else :
                stack.append(i)
        elif i == "}" :
            if stack[-1] == "{" :
                stack.pop()
            else :
                stack.append(i)
        elif i == ")" :
            if stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(i)
        else :
            stack.append(i)
    
    return stack

def solution(s):
    result = 0
    s = list(s)
    for i in range(len(s)) :
        s.append(s.pop(0))
        temp = stack_F(s)
        if temp == [0] :
            result += 1
    
    return result