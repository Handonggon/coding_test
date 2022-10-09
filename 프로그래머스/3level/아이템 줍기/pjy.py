from collections import deque
def solution(rec, characterX, characterY, itemX, itemY):
    
    co = [['0' for i in range(102)] for i in range(102)] #0으로 이루어진 도화지


    #직사각형을 주는 리스트를 항상 형식이 같게끔 정렬
    for i in range(len(rec)):
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

    # 분별력을 높이기위해 크기를 두배로 늘림
    for i in range(len(rec)): 
        for j in range(len(rec[i])):
            rec[i][j] = rec[i][j]*2




    #0으로 이루어진 도화지에 "f"로 그림을 그림
    for i in rec: 
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

    #길을 만들기전 시작점 설정
    start = [rec[0][0],rec[0][1]]
    for i in rec: 
        if start[0] <= i[0]:
            pass
        else:
            start = [i[0],i[1]]

    move =[[0,1],[1,0],[0,-1],[-1,0]] #위,오른쪽,아래,왼쪽 순서 이유는 미로에서 오른손의 법칙처럼 계속 오른쪽으로만 가게되면 결국 길을 찾게 된다.
    count = 0 
    way = start.copy()
    comeback = 0

    #현재 진행방향의 왼쪽부터 탐색
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

    # 지도의 크기가 두배가 되었기때문에 나머지 좌표도 2배로 만든다
    cxy = [characterX*2,characterY*2,0] 
    ixy = [itemX*2,itemY*2]

    enter = [(0,1),(0,-1),(-1,0),(1,0)] #위 아래 왼쪽 오른쪽

    queue = deque([])

    # queue 의 초기값 설정
    co[cxy[1]][cxy[0]] = "true"
    for i in enter:
        if co[cxy[1]+i[1]][cxy[0]+i[0]] == 'w':
            queue.append([cxy[0]+i[0],cxy[1]+i[1],cxy[2]+1])
        else:
            pass
    while queue != []:
        a = queue.popleft()
        if a[:2] == ixy:
            return int(a[2]/2)
        co[a[1]][a[0]] = 'true'
        for i in enter:
            if co[a[1]+i[1]][a[0]+i[0]] == 'w':
                queue.append([a[0]+i[0],a[1]+i[1],a[2]+1])