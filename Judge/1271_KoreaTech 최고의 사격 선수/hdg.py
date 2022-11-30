import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

#N = 9
#info = [[-3, -3], [2, 3], [-2, -2], [5, 7], [-1, -1], [-1, -1], [0, -1], [-1, 0], [10, 10]]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

answer = 0
for i in range(N):
    twins = 0
    table = {}
    for j in range(i, N):
        dx = info[j][0] - info[i][0]
        dy = info[j][1] - info[i][1]
        if dx == 0 and dy == 0:
            twins += 1
            continue
        
        if dx == 0:
            key = 'V'
        elif dy == 0:
            key = 'H'
        else:
            key = ''
            r = gcd(abs(dy), abs(dx))
            if (dy < 0) ^ (dx < 0) :
                key += '-'
            key += str(abs(dy // r)) + '/' + str(abs(dx // r))

        if key not in table:
            table[key] = 0
        table[key] += 1
    
    answer = max(twins, answer)
    if table:
        answer = max(max(table.values()) + twins, answer)
print(answer)