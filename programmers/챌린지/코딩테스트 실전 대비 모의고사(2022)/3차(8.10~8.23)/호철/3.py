def solution(distance, scope, times):
    res = [distance]

    for i in range(len(scope)):
        a = times[i][0]
        min_s = min(scope[i])
        max_s = max(scope[i])

        if min_s <= a <= max_s:
            res.append(min_s)
            
        elif a < min_s:
            a += times[i][1]
            b = min_s // a
            for j in range(1, times[i][0]+1):
                c = b * a + j
                if min_s <= c <= max_s:
                    res.append(c)
                    break
            b = max_s // a
            for j in range(1, times[i][0]+1):
                c = b * a + j
                if min_s <= c <= max_s:
                    res.append(c)
                    break

        elif a > max_s:
            res.append(min_s)

    return min(res)