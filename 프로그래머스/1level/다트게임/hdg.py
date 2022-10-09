import math

def solution(dartResult):
    stack = []
    
    index = 0
    while index < len(dartResult):
        if dartResult[index].isnumeric():
            number = int(dartResult[index])
            if number == 1 and dartResult[index+1] == '0':
                stack.append(10)
                index += 1
            else:
                stack.append(number)
        else:
            if dartResult[index] == 'S':
                stack.append(pow(stack.pop(), 1))
            elif dartResult[index] == 'D':
                stack.append(pow(stack.pop(), 2))
            elif dartResult[index] == 'T':
                stack.append(pow(stack.pop(), 3))
            elif dartResult[index] == '*':
                curr = stack.pop()
                if len(stack):
                    stack.append(stack.pop() * 2)
                stack.append(curr * 2)
            elif dartResult[index] == '#':
                stack.append(stack.pop() * -1)
        index += 1
    return sum(stack)
