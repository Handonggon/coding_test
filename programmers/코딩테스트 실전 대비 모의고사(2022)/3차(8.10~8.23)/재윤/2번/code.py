def solution(ing):
    answer = 0
    cook = []
    for i in ing:
        cook.append(i)
        while len(cook)>=4:
            a = cook.pop()
            b = cook.pop()
            c = cook.pop()
            d = cook.pop()
            if a == 1 and b == 3 and c == 2 and d == 1:
                answer += 1
            else:
                cook.append(d)
                cook.append(c)
                cook.append(b)
                cook.append(a)
                break
    return answer