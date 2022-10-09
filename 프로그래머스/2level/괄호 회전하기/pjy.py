def wrap(list_w,p):
    if list_w[-1] == '[':
        if p == ']':
            return True
        else:
            return False
    elif list_w[-1] == '{':
        if p == '}':
            return True
        else:
            return False
    elif list_w[-1] == "(":
        if p == ')':
            return True
        else:
            return False
    else:
        return False

def solution(s):
    stack = []
    answer = 0
    a = []
    for i in s:
        a.append(i)
    count = len(a)
    while count != 0:
        possible = True
        for i in a:
            if len(stack) > 0:
                if wrap(stack,i) == True:
                    stack.pop()
                else:
                    if i == "[" or i == "{" or i == "(":
                        stack.append(i)
                    else:
                        possible = False
                        break
            else:
                if i == "[" or i == '{' or i == "(":
                    stack.append(i)
                else:
                    possible = False
                    break
        if possible == True and stack == []:
            answer += 1
        else:
            pass
        
        a.append(a.pop(0))
        
        count -= 1
        
    return answer