def solution(ingredient):
    stack_list = []
    result = 0
    for i in range(len(ingredient)) :
        stack_list.append(ingredient[i])
        if len(stack_list) >= 4 :
            if stack_list[-4:] == [1,2,3,1] :
                stack_list.pop()
                stack_list.pop()
                stack_list.pop()
                stack_list.pop()
                result += 1
    return result