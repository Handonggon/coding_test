rec = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
co = [['0' for i in range(40)] for i in range(40)] #0으로 이루어진 도화지
rec = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
for i in range(len(rec)): #직사각형을 주는 리스트를 항상 형식이 같게끔 정렬
    hlx = rec[i][0]
    hly = rec[i][1]
    hrx = rec[i][2]
    hry = rec[i][3]
    if hlx < hrx:
        pass
    else:
        rec[i][0] = hrx
        rec[i][1] = hry
        rec[i][2] = hlx
        rec[i][3] = hlx
for i in range(len(rec)): # 분별력을 높이기위해 크기를 두배로 늘림
    for j in range(len(rec[i])):
        rec[i][j] = rec[i][j]*2





for i in rec: #0으로 이루어진 도화지에 "f"로 그림을 그림
    a = [i[0],i[1]]
    co[a[1]][a[0]] = 'f'
    while a[0] != i[2]:
        a[0] += 1
        co[a[1]][a[0]] = 'f'
    while a[1] != i[3]:
        a[1] += 1
        co[a[1]][a[0]] = 'f'
    while a[0] != i[0]:
        a[0] -= 1
        co[a[1]][a[0]] = 'f'
    while a[1] != i[1]:
        a[1] -= 1
        co[a[1]][a[0]] = 'f'

start = [rec[0][0],rec[0][1]]
for i in rec: #길을 만들기전 시작점 설정
    if start[0] <= i[0]:
        pass
    else:
        start = [i[0],i[1]]

move =[[0,1],[1,0],[0,-1],[-1,0]] #위,오른쪽,아래,왼쪽 순서 이유는 미로에서 오른손의 법칙처럼 계속 오른쪽으로만 가게되면 결국 길을 찾게 된다.
count = 0 
way = start.copy()
comeback = 0
while comeback == 0: 
    co[way[1]][way[0]] = "w"
    if co[way[1]+move[(count-1)%4][1]][way[0]+move[(count-1)%4][0]] == "f":
        way[1] += move[(count-1)%4][1]
        way[0] += move[(count-1)%4][0]
        count -= 1
    elif co[way[1]+move[(count)%4][1]][way[0]+move[(count)%4][0]] == "f":
        way[1] += move[(count)%4][1]
        way[0] += move[(count)%4][0]
    elif co[way[1]+move[(count+1)%4][1]][way[0]+move[(count+1)%4][0]] == "f":
        way[1] += move[(count+1)%4][1]
        way[0] += move[(count+1)%4][0]
        count += 1
    else:
        break