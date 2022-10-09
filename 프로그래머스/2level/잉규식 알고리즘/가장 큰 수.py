def solution(numbers):
    result = ''
    length = len(str(max(numbers)))
    numbers = [str(i) for i in numbers]
    for i in range(len(numbers)) :
        count = 0
        while len(numbers[i]) <= length :
            count += len(numbers[i])
            numbers[i] += numbers[i]
        numbers[i] = [numbers[i],count]
    numbers = sorted(numbers,reverse=True)
    for i in range(len(numbers)) :
        for j in range(numbers[i][1]) :
            numbers[i][0] = numbers[i][0][:-1]
        result += numbers[i][0]
    
    return str(int(result))