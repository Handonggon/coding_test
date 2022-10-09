def solution(board):
    answer = 0
    count = min(len(board),len(board[0]))
    while count != 0:
        square = [[1 for i in range(count)] for i in range(count)]
        for i in range(len(board)): #세로길이
            for j in range(len(board[0])): #가로길이
                if j+count > len(board[0]) or i+count > len(board):
                    break
                else:
                    a = [[n for n in board[m][j:j+count]] for m in range(i,count+i)]
                    if a == square:
                        return count*count
                    else:
                        pass
        count -= 1
    return 0
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 조건 추가후에도 시간초과
def solution(board):
    answer = 0
    s = len(board)
    g = len(board[0])
    count = min(s,g)
    while count != 0:
        square = [[1 for i in range(count)] for i in range(count)]
        for i in range(s): #세로길이
            for j in range(g): #가로길이
                if j+count > g or i+count > s:
                    break
                else:
                    if board[i][j:j+count] == [1 for i in range(count)] and [[board[i][j]] for i in range(i,count+i)] == [[1] for i in range(count)]:
                        a = [[n for n in board[m][j:j+count]] for m in range(i,count+i)]
                        if a == square:
                            return count*count
                        else:
                            pass
                    else:
                         pass   
        count -= 1
    return 0