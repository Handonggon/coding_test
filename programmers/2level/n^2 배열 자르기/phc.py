res = []

def fun(a, b):
    global res
    if b <= a:
        res.append(a+1)
    elif b > a:
        res.append(b+1)

def solution(n, left, right):
    global res
    a, b = left // n, left % n
    
    for _ in range(right-left+1):
        if b == n:
            a , b = a+1, 0
            fun(a, b)
            b+=1
        else:
            fun(a, b)
            b+=1
            
    return res  