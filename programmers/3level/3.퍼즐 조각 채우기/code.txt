game_board = [[0,0,0],[1,1,0],[1,1,1]]
table = [[1,1,1],[1,0,0],[0,0,0]]

find = [[0 for i in game_board] for i in game_board] # 도형하나하나 그려넣을 흰도화지 만들기
figures = table.copy() #도형들의 집합
for i in range(len(find)): # 도형 시작점 찾기
    for j in range(len(find)):
        if figures[i][j] == 1:
            start = [i,j]
            break
    break
queue = deque([start])
l = len(table)-1
while queue != deque([]):
    a = queue.popleft()
    figures[a[1]][a[0]] = 0 #도형들이 모여있는곳에서
    find[a[1]][a[0]] = 1 #하나씩 옮기자
    if a[0] != l: #start점의 x좌표가 끝자락이 아니라면
        if figures[a[1]][a[0]+1] == 1:
            queue.append([a[0]+1,a[1]])
    if a[0] != 0: #start점의 x좌표가 처음이 아니라면
        if figures[a[1]][a[0]-1] == 1:
            queue.append([a[0]-1,a[1]])
    if a[1] != l: #start점의 y좌표가 끝자락이 아니라면
        if figures[a[1]+1][a[0]] == 1:
            queue.append([a[0],a[1]+1])
    if a[1] != 0: #start점의 y좌표가 처음이 아니라면
        if figures[a[1]-1][a[0]] == 1:
            queue.append([a[0],a[1]-1])
count = 0
while count < len(find):
    if find[count] == [0 for i in range(len(find[0]))]:
        find.pop(count)
    else:
        count += 1
count = 0
while count < len(find[0]): #도화지에서 흰곳 뺴기
    for i in range(len(find)):
        if find[i][count] == 0:
            if i == len(find)-1:
                for i in find:
                    i.pop(count)
        else:
            count += 1
            break

##도형하나 구하기

find = [[0 for i in game_board] for i in game_board] # 도형하나하나 그려넣을 흰도화지 만들기
figures = table #도형들의 집합
start = []
for i in range(len(find)): # 도형 시작점 찾기
    for j in range(len(find)):
        if figures[j][i] == 1:
            start.append(i)
            start.append(j)
            break
        else:
            pass
    if len(start)>0:
        break

queue = deque([start])
l = len(table)-1
while queue != deque([]):
    a = queue.popleft()
    figures[a[1]][a[0]] = 0 #도형들이 모여있는곳에서
    find[a[1]][a[0]] = 1 #하나씩 옮기자
    if a[0] != l: #start점의 x좌표가 끝자락이 아니라면
        if figures[a[1]][a[0]+1] == 1:
            queue.append([a[0]+1,a[1]])
    if a[0] != 0: #start점의 x좌표가 처음이 아니라면
        if figures[a[1]][a[0]-1] == 1:
            queue.append([a[0]-1,a[1]])
    if a[1] != l: #start점의 y좌표가 끝자락이 아니라면
        if figures[a[1]+1][a[0]] == 1:
            queue.append([a[0],a[1]+1])
    if a[1] != 0: #start점의 y좌표가 처음이 아니라면
        if figures[a[1]-1][a[0]] == 1:
            queue.append([a[0],a[1]-1])
count = 0
while count < len(find): #도화지에서 흰곳 뺴기
    if find[count] == [0 for i in range(len(find[0]))]:
        find.pop(count)
    else:
        count += 1
count = 0
while count < len(find[0]): #도화지에서 흰곳 뺴기
    for i in range(len(find)):
        if find[i][count] == 0:
            if i == len(find)-1:
                for i in find:
                    i.pop(count)
        else:
            count += 1
            break
count = 0
figure = []
while count != 4:
    a = find
    figure.append(a)
    count += 1
    find = [[find[j][i] for j in range(len(find)-1,-1,-1)] for i in range(len(find[0]))]

same = []

for i in space:
    for j in figure:
        if i == j:
            same.append(i)
            break
        else:
            pass
    if len(same) > 0:
        break
