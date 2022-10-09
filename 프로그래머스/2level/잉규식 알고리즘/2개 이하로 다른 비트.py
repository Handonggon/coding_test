def solution(numbers):
    for i in range(len(numbers)) :
        if numbers[i]%2 == 0 :
            numbers[i] += 1
        else :
            numbers[i] = bin(numbers[i])
            if numbers[i].count('0') == 1 :
                numbers[i] = numbers[i][:3] + '0' + numbers[i][3:]
            else :
                numbers[i] = list(numbers[i])
                for j in range(len(numbers[i])-1,2,-1) :
                    if numbers[i][j] == '0' :
                        numbers[i][j] = '1'
                        numbers[i][j+1] = '0'
                        break
                numbers[i] = ''.join(numbers[i])
            numbers[i] = int(numbers[i],2)

    return numbers