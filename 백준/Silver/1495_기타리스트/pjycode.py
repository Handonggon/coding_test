from collections import deque
import pstats
N,S,M = input().split(" ")
list_v = deque(input().split(" "))
list_n = ["True" for i in range(int(M)+1)]
list_n[int(S)] = "False"
while list_v != deque([]):
    a = int(list_v.popleft())
    count = 0
    list_c = ["True" for i in range(int(M)+1)]
    while count != int(M)+1:
        if list_n[count] == "True":
            pass
        else:
            if 0<=count+a<=int(M):
                list_c[count+a] = "False"
            if 0<=count-a<=int(M):
                list_c[count-a] = "False"
        count += 1
    list_n = list_c.copy()
for i in range(len(list_n)-1,-1,-1):
    if list_n[i] == "False":
        print(i)
        break
    else:
        pass
    if i == 0:
        print(-1)
