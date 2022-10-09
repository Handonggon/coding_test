def solution(sur, cho):
    answer = ''
    
    dict ={'R':0,
           'T':0,
           'C':0,
           'F':0,
           'J':0,
           'M':0,
           'A':0,
           'N':0}
    for i in range(len(sur)):
        if cho[i] <=4:
            dict[sur[i][0]] += 4-cho[i]
        else:
            dict[sur[i][1]] += cho[i]-4
    if dict['R'] >= dict['T']:
        answer += "R"
    else:
        answer += 'T'
    if dict['C'] >= dict['F']:
        answer += "C"
    else:
        answer += 'F'
    if dict['J'] >= dict['M']:
        answer += "J"
    else:
        answer += 'M'
    if dict['A'] >= dict['N']:
        answer += "A"
    else:
        answer += 'N'
    
            
    return answer