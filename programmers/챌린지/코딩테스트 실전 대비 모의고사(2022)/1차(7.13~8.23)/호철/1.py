def solution(X, Y):
    X = str(X)
    Y = str(Y)

    dic = {}
    for i in range(10):
        a = X.count(str(i))
        b = Y.count(str(i))

        if a and b:
            if a >= b:
                dic[i] = b
            else:
                dic[i] = a

    if dic == {}: return str(-1)

    ans =''
    for i in range(10):
        if dic.get(i) != None:
            ans = str(i) * dic.get(i) + ans
    
    if ans[0] == '0': return str(0)


    return ans