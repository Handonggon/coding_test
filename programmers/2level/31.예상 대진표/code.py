def solution(n,a,b):
    if a > b:
        a,b = b,a
    count = 0
    while n != 1:
        count += 1
        n = n/2
    n = 2**count

    while count != 0:
        if 0<a<=2**(count-1) and 2**(count-1)<b<=2**count:
            return count
            break
        elif 2**(count-1)<a and 2**(count-1)<b:
            a -= 2**(count-1)
            b -= 2**(count-1)
        else:
            pass
        
        count -= 1
    return count