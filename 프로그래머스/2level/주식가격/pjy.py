def solution(prices):
    answer = [0 for i in prices]
    stack = []
    prices_index = []
    for i in range(len(prices)-1,-1,-1):
        prices_index.append([prices.pop(),i])


    while prices_index != []:
        a = prices_index.pop()
        if stack == []:
            stack.append(a)
        else:
            while True:
                if stack == []:
                    stack.append(a)
                    break
                b = stack.pop()
                if b[0] <= a[0]:
                    stack.append(b)
                    stack.append(a)
                    break
                else:
                    answer[b[1]] = a[1] - b[1]
    a = stack.pop()
    while stack != []:
        b = stack.pop()

        answer[b[1]] = a[1] - b[1]
    return answer