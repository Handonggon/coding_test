import sys
input = sys.stdin.readline

[E, EM, M, MH, H] = map(int, input().split())

count = 0
while True:
    if E > 0:
        E -= 1
    else:
        if EM > 0:
            EM -= 1
        else:
            break
    
    if H > 0:
        H -= 1
    else:
        if MH > 0:
            MH -= 1
        else:
            break
    
    if M > 0:
        M -= 1
    else:
        if EM > MH and EM > 0:
            EM -= 1
        elif MH > EM and MH > 0:
            MH -= 1
        elif EM == MH and EM > 0:
            EM -= 1
        else:
            break
    count += 1
print(count)