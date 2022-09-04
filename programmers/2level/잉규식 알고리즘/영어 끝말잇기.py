def solution(n, words):
    log = [words[0]]
    TF = True
    for idx in range(1,len(words)) :
        if words[idx] not in log :
            if words[idx-1][-1] == words[idx][0] :
                log.append(words[idx])
            else :
                TF = False
                break
        else :
            TF = False
            break
    print(idx)
    if TF :
        return [0,0]
    else :
        return [idx%n+1,idx//n+1]