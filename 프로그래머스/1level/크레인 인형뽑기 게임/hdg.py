def solution(board, moves):
    stack = []
    answer = 0
    
    for move in moves:
        for index in range(len(board)):
            if board[index][move-1] > 0:
                stack.append(board[index][move-1])
                board[index][move-1] = 0
                
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break
    return answer
