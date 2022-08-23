def solution(s,c):
    dic={'R':0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}

    for i in range(len(s)):
        if c[i] == 5: dic[s[i][1]] += 1
        elif c[i] == 6: dic[s[i][1]] += 2
        elif c[i] == 7: dic[s[i][1]] += 3
        elif c[i] == 3: dic[s[i][0]] += 1
        elif c[i] == 2: dic[s[i][0]] += 2
        elif c[i] == 1: dic[s[i][0]] += 3
    ans = ''
    if dic.get("R") < dic.get("T"):
        ans += "T"
    else: ans += "R"
    if dic.get("C") < dic.get("F"):
        ans += "F"
    else: ans += "C"
    if dic.get("J") < dic.get("M"):
        ans += "M"
    else: ans += "J"
    if dic.get("A") < dic.get("N"):
        ans += "N"
    else: ans += "A"

    return ans