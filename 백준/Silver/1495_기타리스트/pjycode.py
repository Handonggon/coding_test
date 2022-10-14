from collections import deque
N,S,M = input().split(" ")
list_v = deque(input().split(" "))
list_n = deque([int(S)])
while list_v != deque([]):
    a = int(list_v.popleft())
    count = len(list_n)
    if count == 0:
        break
    while count != 0:
        b = list_n.popleft()
        c = b+a
        if 0<=c<=int(M):
            list_n.append(c)
        else:
            pass
        c = b-a
        if 0<=c<=int(M):
            list_n.append(c)
        else:
            pass
        count -= 1
if len(list_n) == 0:
    print(-1)
else :
    print(max(list_n))
