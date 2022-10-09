def solution(n, arr1, arr2):
    answer = []
    for index in range(n):
        answer.append(arr1[index] | arr2[index])
        answer[index] = format(answer[index], 'b').zfill(n).replace('1', '#').replace('0', ' ')
    return answer
