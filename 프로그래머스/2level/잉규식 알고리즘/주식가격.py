def solution(prices):
    result = [0 for i in range(len(prices))]
    for i in range(len(prices)) :
        count = 0
        for j in range(i+1,len(prices)) :
            if prices[i] <= prices[j] :
                count += 1
            else : 
                count += 1
                break
        result[i] = count 
    return result