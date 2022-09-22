from collections import deque
def solution(p):
    list_w = deque([])
    for i in p:
        list_w.append(i)
    u = deque([])
    v = list_w
    answer = []
    while v != deque([]):
        count = 0
        a = v.pop()
        u.append(a)
        if a == '(':
            count += 1
        else:
            count -= 1
        
        while count != 0 and len(v) > 0:
            a = v.pop()
            if a == "(":
                count += 1
            else:
                count -= 1
            u.appendleft(a)

        correct = True
        count = 0
        for i in u:
            if i == "(":
                count += 1
            else:
                count -= 1
            
            if count < 0:
                correct = False
                break
        
        if correct == False:
            m = "("
            if len(answer) == 0:
                m += ")"
            else:
                m += answer.pop()
                m += ")"
            u.popleft()
            u.pop()
            for i in range(len(u)):
                if u[i] == "(":
                    u[i] = ")"
                else:
                    u[i] = "("
            for i in u:
                m += i
            answer.append(m)
        else:
            m = ""
            for i in u:
                m += i
            if len(answer) > 0:
                a = answer.pop()
                b = m+a
                answer.append(b) 
            
            else:
                answer.append(m)


        u = deque([])

        

    return answer[0]