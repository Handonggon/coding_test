def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{') 
    for i in range(len(s)) :
        s[i] = set(s[i].split(','))
    s.sort()
    result = []
    for i in s :
        for j in i :
            if int(j) not in result :
                result.append(int(j))
    return result