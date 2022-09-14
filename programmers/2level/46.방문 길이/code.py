def solution(dirs):
    a = [["True" for j in range(31)] for i in range(31)]
    answer = 0
    start = [15,15]
    a[15][15] = 'False'
    move = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
    for i in dirs:
        start[0] += move[i][0]
        start[1] += move[i][1]
        if start[0] == -1:
            start[0] = 0
        elif start[1] == -1:
            start[1] = 0
        elif start[0] == 31:
            start[0] = 30
        elif start[1] == 31:
            start[1] = 30
        else:
            pass
        if a[start[0]][start[1]] == "True":
            answer += 1
            a[start[0]][start[1]] = "False"
        else:
            pass
        start[0] += move[i][0]
        start[1] += move[i][1]
        if start[0] == -1:
            start[0] = 0
        elif start[1] == -1:
            start[1] = 0
        elif start[0] == 31:
            start[0] = 30
        elif start[1] == 31:
            start[1] = 30
        else:
            pass
        a[start[0]][start[1]] = "False"
        
        start[0] += move[i][0]
        start[1] += move[i][1]
        if start[0] == -1:
            start[0] = 0
        elif start[1] == -1:
            start[1] = 0
        elif start[0] == 31:
            start[0] = 30
        elif start[1] == 31:
            start[1] = 30
        else:
            pass
        a[start[0]][start[1]] = "False"
    return answer