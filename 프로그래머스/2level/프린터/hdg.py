def solution(pr, lo):
    answer = 0
    tg = [False for i in range(len(pr))]
    tg[lo] = True # tg = [False, False, True, False]
    while pr != []:
        if max(pr) == pr[0]:
            pr.pop(0)
            answer += 1
            n = tg.pop(0)
            if n:
                return answer
        else:
            pr.append(pr.pop(0))
            tg.append(tg.pop(0))