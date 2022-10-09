def solution(arr1,arr2):
    answer = [[0 for i in arr1[0]] for i in arr1] # arr1[0]의 크기만큼 0 의 리스트를 만들고 arr1크기만큼 []를 만듦 
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer