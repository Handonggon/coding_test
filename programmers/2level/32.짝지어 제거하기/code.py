def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while True:
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                if a == b:
                    pass
                else:
                    stack.append(b)
                    stack.append(a)
                    break
            else:
                break
    if stack == []:
        return 1
    else:
        return 0