def solution(s):
    total = 0
    box = []
    while len(s)>1:
        ans = ''
        cnt = 0
        for i in s:
            if i == "1": ans += "1"
            else: cnt += 1
        box.append(cnt)
        s = bin(len(ans))[2:]
        total += 1
        
    return [total, sum(box)]