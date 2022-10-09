def solution(order):
    first = [i for i in range(max(order),0,-1)]
    bojo = [0]
    count = 0
    for i in order :
        if bojo[-1] > i :
            break
        else :
            while bojo[-1] != i :
                bojo.append(first.pop())
            bojo.pop()
            count += 1
    return count 