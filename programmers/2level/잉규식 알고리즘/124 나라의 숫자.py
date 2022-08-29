def solution(n):
    rev_base = ''
    number = ['1','2','4']
    while n > 0:
        n -= 1
        n, mod = divmod(n, 3)
        rev_base += str(number[mod])

    return rev_base[::-1] 