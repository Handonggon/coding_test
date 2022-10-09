from collections import deque
def solution(maps):
    find = [[0 for i in range(len(maps[0]))] for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                find[i][j] = 'true'
            else:
                find[i][j] = 'false'

    move = [[-1,0],[1,0],[0,-1],[0,1]]
    queue = deque([[0,0,1]])
    find[0][0] = 'false'
    count = 0 
    while queue != deque([]):
        count += 1
        a = queue.popleft() # [0,0,1]
        if a[0] == len(maps)-1 and a[1] == len(maps[0])-1:
            return a[2]
        for i in move: # [-1,0],[1,0],[0,-1],[0,1]
            dy = a[0]+i[0]
            dx = a[1]+i[1]
            if 0<=dy<len(find) and 0<=dx<len(find[0]):
                if find[dy][dx] == 'true':
                    find[dy][dx] = 'false'
                    queue.append([dy,dx,a[2]+1])
    return -1