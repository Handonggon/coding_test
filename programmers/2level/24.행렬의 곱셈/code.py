def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            count = 0
            while count != len(arr1[0]):
                answer[i][j] += arr1[i][count] * arr2[count][j]
                count += 1
            
    
    return answer