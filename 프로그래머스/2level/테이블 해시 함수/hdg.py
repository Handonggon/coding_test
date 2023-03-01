def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda row: (row[col - 1], -row[0]))
    
    answer = 0
    for i in range(row_begin - 1, row_end):
        S_i = 0
        for item in data[i]:
            S_i += (item % (i + 1))
        answer = (answer ^ S_i)
    return answer