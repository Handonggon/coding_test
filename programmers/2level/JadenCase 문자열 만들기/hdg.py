def solution(s):
    s = list(s)
    count = 0
    for i in range(len(s)):
        if count ==0:
            if s[i].isdigit():
                count +=1
            elif s[i].isalpha():
                s[i] = s[i].upper()
                count += 1
            else:
                count = 0
        else:
            if s[i].isdigit():
                count +=1
            elif s[i].isalpha():
                s[i] = s[i].lower()
            else:
                count = 0
                
    answer =''
    for i in s:
        answer += i
    return answer