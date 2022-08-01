def solution(dartResult):
    da = dartResult
    stacks = []
    stacks_ans = []
    for i in range(len(da)):
        if da[i].isdigit():
            if da[i+1].isdigit():
                stacks.append('10')
            else:
                stacks.append(da[i])
            
            if len(stacks) == 2:
                stacks.pop()
            
        elif da[i].isalpha() == True:
            a = int(stacks.pop())
            
            if da[i] == "D":
                stacks_ans.append(pow(a, 2))
            elif da[i] == "T":
                stacks_ans.append(pow(a,3))
            else:
                stacks_ans.append(a)

        else:
            if da[i] == '*':
                if len(stacks_ans) >= 2:
                    f = stacks_ans.pop()*2
                    s = stacks_ans.pop()*2

                    stacks_ans.append(s)
                    stacks_ans.append(f)
                else:
                    stacks_ans.append(stacks_ans.pop()*2)

            elif da[i] == '#':
                stacks_ans.append(stacks_ans.pop()*(-1))

    return sum(stacks_ans)