from collections import deque
def solution(str1, str2):
    str1l = deque([])
    str2l = deque([])
    jset_1 = []
    jset_2 = []
    for i in str1:
        str1l.append(i)
    for i in str2:
        str2l.append(i)
    while str1l != deque([]):
        el = ""
        if 1 < len(str1l):
            a = str1l.popleft()
            b = str1l.popleft()
            if a.isalpha() == True and b.isalpha() == True:
                el += a+b
                jset_1.append(el.lower())
            str1l.appendleft(b)
        else:
            break
    while str2l != deque([]):
        el = ""
        if 1 < len(str2l):
            a = str2l.popleft()
            b = str2l.popleft()
            if a.isalpha() == True and b.isalpha() == True:
                el += a+b
                jset_2.append(el.lower())
            str2l.appendleft(b)
        else:
            break
    dict = {}
    for i in jset_1:
        dict[i] = 0
    for i in jset_2:
        dict[i] = 0
    union = 0
    intersection = 0
    # 합집합 구하기
    for i in jset_1:
        dict[i] += 1
        union += 1
    for i in jset_2:
        if dict[i] == 0:
            union += 1
        else:
            dict[i] -= 1
    #초기화
    for i in dict:
        dict[i] = 0
    #교집합 구하기
    for i in jset_1:
        dict[i] += 1
    for i in jset_2:
        if dict[i] > 0:
            dict[i] -= 1
            intersection += 1
        else:
            pass
    if intersection == 0 and union == 0:
        return 65536
    ja = intersection/union
    return int(ja*65536)