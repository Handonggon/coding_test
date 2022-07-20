def solution(s, n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(s)):
        for j in range(len(a)):
            if s[i] == a[j]:   
                s = list(s)
                s[i] = a[(j+n)%len(a)]
                s = ''.join(s)
                break
    for i in range(len(s)):
        for j in range(len(b)):
            if s[i] == b[j]:   
                s = list(s)
                s[i] = b[(j+n)%len(b)]
                s = ''.join(s)
                break
        
    
    
    return s