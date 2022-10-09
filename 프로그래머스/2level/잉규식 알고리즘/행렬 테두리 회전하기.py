def solution(rows, columns, queries):
    arr = [i for i in range(1,rows*columns+1)]
    answer = []
    for i in queries :
        temp = []
        idx_list = []
        p = (i[0]-1)*columns+i[1]
        for j in range(i[3]-i[1]+1) :
            idx_list.append(p)
            p += 1
        start = i[0]
        while start < i[2] - 1 :
            idx_list.append(start*columns + i[1])
            idx_list.append(start*columns + i[3])
            start += 1
        p = (i[2]-1)*columns+i[1]
        for j in range(i[3]-i[1]+1) :
            idx_list.append(p)
            p += 1
        start = i[0]
        temp.append(arr[start*columns + i[1]-1])
        idx = (i[0]-1)*columns+i[1]
        for j in range(i[3]-i[1]) :
            temp.append(arr[idx-1])
            idx += 1
        while start < i[2] - 1:
            start += 1
            temp.append(arr[start*columns + i[1]-1])
            temp.append(arr[idx-1])
            idx += columns
        idx2 = (i[2]-1)*columns+i[1] + 1
        for j in range(i[3]-i[1]) :
            temp.append(arr[idx2-1])
            idx2 += 1
        temp.append(arr[idx-1])
        answer.append(min(temp))
        for j in range(len(idx_list)) :
            arr[idx_list[j]-1] = 0
        for j in range(len(arr)) :
            if arr[j] == 0 :
                arr[j] = temp.pop(0)
    
    return answer  
        