def solution(commands):
    list_w = [[["",(i,j)] for j in range(51)] for i in range(51)]
    answer = []
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 3: # value 1을 value 2로 바꿉니다
                v1 = command[1]
                v2 = command[2]
                for r in range(1,51):
                    for c in range(1,51):                   
                        if list_w[r][c][0] == v1: # value1이라면 value2로                        
                            for i in list_w[r][c][1:]:
                                list_w[i[0]][i[1]][0] = v2 #그부분도 value2로 바꾸기
            else: #r c 를 value로 바꿉니다
                r = int(command[1])
                c = int(command[2])
                v = command[3]
                for i in list_w[r][c][1:]:
                    list_w[i[0]][i[1]][0] = v #value2로 바꾸기
                

        elif command[0] == "MERGE": # r1,c1과 r2,c2를 병합합니다
            r1 = int(command[1])
            c1 = int(command[2])
            r2 = int(command[3])
            c2 = int(command[4])
            if list_w[r1][c1][0] != "" and list_w[r2][c2][0] != "":
                list_w[r2][c2][0] = list_w[r1][c1][0]
            elif list_w[r1][c1][0] != "" and list_w[r2][c2][0] == "":
                list_w[r2][c2][0] = list_w[r1][c1][0]
            elif list_w[r1][c1][0] == "" and list_w[r2][c2][0] != "":
                list_w[r1][c1][0] = list_w[r2][c2][0]
            else:
                pass

            
            for i in list_w[r1][c1][1:]:
                list_w[i[0]][i[1]][0] = list_w[r1][c1][0] 
            for i in list_w[r2][c2][1:]:
                list_w[i[0]][i[1]][0] = list_w[r1][c1][0]

            for i in list_w[r1][c1][1:]:
                for j in list_w[r2][c2][1:]:
                    list_w[i[0]][i[1]].append(j)
            for i in list_w[r2][c2][1:]:
                for j in list_w[r1][c1][1:]:
                    list_w[i[0]][i[1]].append(j)

            

        elif command[0] == "UNMERGE": # r,c를 포함한 셀의 병합을 해제합니다
            r = int(command[1])
            c = int(command[2])
            for i in list_w[r][c][2:]:
                list_w[i[0]][i[1]] = ["",(i[0],i[1])]
            list_w[r][c] = [list_w[r][c][0],(r,c)]

        else: # "PRINT"
            r = int(command[1])
            c = int(command[2])
            if list_w[r][c][0] != "":
                answer.append(list_w[r][c][0])
            else:
                answer.append("EMPTY")

    return answer