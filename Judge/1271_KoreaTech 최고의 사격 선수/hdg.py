N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

#N = 5
#info = [[-3, -3], [2, 3], [-2, -2], [5, 7], [-1, -1]]

answer = [[0, 0, 0, 0] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        dy = info[j][0] - info[i][0]
        dx = info[j][1] - info[i][1]

        if dx == 0 and dy == 0:
            answer[i] = map(lambda x: x+1, answer[i])
            answer[j] = map(lambda x: x+1, answer[j])
        elif dy == 0:
            answer[i][0] += 1
            answer[j][0] += 1
        elif dx == 0:
            answer[i][1] += 1
            answer[j][1] += 1
        else:
            a = dy / dx
            if a == 1:
                answer[i][2] += 1
                answer[j][2] += 1
            elif a == -1:
                answer[i][3] += 1
                answer[j][3] += 1

print(max(list(map(max, answer)))+1)