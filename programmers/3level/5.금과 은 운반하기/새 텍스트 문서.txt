a = 90
b = 500
g = [70,70,0]
s = [0,0,500]
w = [100,100,2]
t = [4,8,1]
time = [0,10000000000000000] # 최댓값 a b를 트럭하나로 옮길떄 걸리는 최대시간 넉넉하게 잡음
tt = [2*i for i in t]
while True:
    if time[0] == time[1]:
        break
    record = []
    c = time[1] - (((time[1] - time[0])//2)+1) # 중간값
    for i in tt:
        round = c//i
        oneway = c%i
        record.append([round,oneway])
    for i in range(len(record)):
        d = record[i][0] * w[i]
        if record[i][1] >= t[i]:
            d += w[i]
        record[i].append(d)
    for i in record:
        z = 0 
        z += i[2]
    if z > a+b:
        time[1] -= ((time[1]-time[0])//2) + 1
    elif z < a+b:
        time[0] += ((time[1]-time[0])//2) + 1
    else:
        break
if time[0] == time[1]:

else:
    

    