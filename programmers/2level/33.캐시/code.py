def solution(cacheSize, cities):
    cache = []
    answer = 0
    citieslower = []
    for i in cities:
        citieslower.append(i.lower())
    
    for i in citieslower:
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:
            if len(cache) >= cacheSize :
                if cacheSize != 0:
                    cache.pop(0)
                    cache.append(i)
                    answer += 5
                else:
                    answer += 5
            else:
                cache.append(i)
                answer += 5
    return answer