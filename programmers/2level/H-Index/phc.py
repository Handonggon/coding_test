def solution(b):
    a = len(b)
    b.sort(reverse=True)
    
    c = []
    ii = a
    while True:
        cnt_1, cnt_2 = 0, 0
        d = ii
        for i in range(a):
            if b[i] >= d: cnt_1 += 1
            else: cnt_2 += 1

        if cnt_1 >= cnt_2 and cnt_2 <= d and cnt_1 >= d: return d
        ii -= 1