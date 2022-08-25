def solution(s):
    
    s = s.split(" ")
    ans = ''
    
    for i in s:
        if i:
            a = i.lower()
            if a[0].isalpha():
                b = a[0].upper()
            else: b = a[0]

            ans += b + a[1::] + " "
        else:
            ans += " "
    
    return ans[0:-1]