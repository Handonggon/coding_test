def solution(m, n, board):
    answer = 0
    for row in range(len(board)) :
        board[row] = list(board[row])
    
    while True :
        index_list = []
        for i in range(m-1) :
            for j in range(n-1) :
                temp = {board[i][j],board[i][j+1],board[i+1][j],board[i+1][j+1]}
                if len(temp) == 1 and type(temp.pop()) == str:
                    index_list.append([i,j])
                    index_list.append([i,j+1])
                    index_list.append([i+1,j])
                    index_list.append([i+1,j+1])
        if index_list == [] :
            return answer
        redundancy = [] 
        for value in index_list:
            if value not in redundancy:
                redundancy.append(value)
        answer += len(redundancy)
        
        for change in redundancy :
            board[change[0]][change[1]] = 0
        for i in range(m-2,-1,-1) :
            for j in range(n) :
                if type(board[i][j]) == str :
                    k = i + 1
                    while k < m and board[k][j] == 0:
                        k += 1
                    pop = board[k-1][j]
                    board[k-1][j] = board[i][j]
                    board[i][j] = pop
