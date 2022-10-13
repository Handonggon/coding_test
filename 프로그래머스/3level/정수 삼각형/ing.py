def solution(triangle):
    dp = triangle[0]
    for i in range(1,len(triangle)) :
        temp1 = triangle[i-1]
        temp2 = [[] for i in range(len(triangle[i]))]
        for j in range(len(temp1)) :
            temp2[j].append(temp1[j] + triangle[i][j])
            temp2[j+1].append(temp1[j] + triangle[i][j+1])
        for j in range(len(temp2)) :
            temp2[j] = max(temp2[j])
        triangle[i] = temp2
    
    return max(triangle[-1])
            