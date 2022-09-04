def solution(order):
    answer = 0
    product = [i for i in range(max(order),0,-1)]
    bozo = []
    for i in order:
        while product != [] or bozo != []:
            if len(product) != 0:
                a = product.pop()
                if a == i:
                    del a
                    answer += 1
                    break
                elif a < i :
                    bozo.append(a)
                else:
                    if bozo == []:
                        return answer
                    product.append(a)
                    if bozo[-1] == i:
                        del bozo[-1]
                        answer += 1
                        break
                    else:
                        return answer
            else:
                if bozo == []:
                    return answer
                if bozo[-1] == i:
                        del bozo[-1]
                        answer += 1
                        break
                else:
                    return answer
        

    return answer