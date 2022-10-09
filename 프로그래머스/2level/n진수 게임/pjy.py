def solution(n, t, m, p):
    a = "0123456789ABCDEF"
    a = a[:n]
    list_n = []
    answer = []
    nn = -1
    tanswer = ''
    z = p-1
    while True:
        nn += 1
        nnn = nn
        if nnn == 0:
            list_n.append("0")
        while nnn != 0:
            list_n.append(a[nnn%n])
            nnn = nnn//n
        while list_n != []:
            answer.append(list_n.pop())
            if len(answer) == t*m:
                break
        if len(answer) == t*m:
            break
    while len(tanswer) != t:
        tanswer += answer[z]
        z += m
    return tanswer