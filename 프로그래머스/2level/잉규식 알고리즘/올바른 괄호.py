def solution(s):
    stack_list = []
    for i in s :
        if i == ")" :
            try:
                stack_list.pop()
            except IndexError:
                return False
        else :
            stack_list.append(i)
    
    return len(stack_list) == 0