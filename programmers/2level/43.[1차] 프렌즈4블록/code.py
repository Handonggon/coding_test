m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
answer = 0
board_reverse = board.copy()
board_reverse.reverse()
list_b = [[0 for j in range(m)] for i in range(n)]
for i in range(len(list_b)):
    for j in range(len(list_b[i])):
        list_b[i][j] = board_reverse[j][i]
# while True:
list_n = []
for i in range(n-1):
    for j in range(m-1):
        a = list_b[i][j]
        b = list_b[i][j+1]
        c = list_b[i+1][j]
        d = list_b[i+1][j+1]
        if a == b == c == d:
            list_n.append([[i,j],[i,j+1],[i+1,j],[i+1,j+1]])
for i in list_n:
    for j in i:
        list_b[j[0]][j[1]] = 0
for i in range(len(list_b)):
    for j in range(len(list_b[i])):
        if list_b[i][j] == 0:
            answer += 1
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def solution(m, n, board):
    answer = 0
    board_reverse = board.copy()
    board_reverse.reverse()
    list_b = [[0 for j in range(m)] for i in range(n)]
    for i in range(len(list_b)):
        for j in range(len(list_b[i])):
            list_b[i][j] = board_reverse[j][i]
    while True:
        list_n = []
        for i in range(n-1):
            for j in range(m-1):
                a = list_b[i][j]
                b = list_b[i][j+1]
                c = list_b[i+1][j]
                d = list_b[i+1][j+1]
                if a == b == c == d:
                    if a != 'space':
                        list_n.append([[i,j],[i,j+1],[i+1,j],[i+1,j+1]])
        if list_n == []:
            break
        for i in list_n:
            for j in i:
                list_b[j[0]][j[1]] = 0
        for i in range(len(list_b)):
            for j in range(len(list_b[i])):
                if list_b[i][j] == 0:
                    answer += 1
        count = 0
        while count != n:
            if 0 in list_b[count]:
                list_b[count].remove(0)
            else:
                count += 1
        count = 0
        while count != n:
            if len(list_b[count]) != m:
                list_b[count].append("space")
            else:
                count += 1
    return answer