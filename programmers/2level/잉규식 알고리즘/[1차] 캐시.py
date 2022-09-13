def solution(cacheSize, cities):
    result = 0
    page = []
    if cacheSize == 0 :
        return len(cities) * 5
    else :
        for idx in range(len(cities)) :
            cities[idx] = cities[idx].lower()
        for city in cities :
            if len(page) < cacheSize :
                if city in page :
                    result += 1
                    page.remove(city)
                else :
                    result += 5
            else :
                if city in page :
                    result += 1
                    page.remove(city)
                else :
                    page.pop(0)
                    result += 5
            page.append(city)
    return result