def solution(citations):
    citations = sorted(citations,reverse=True)
    compare = citations[0]
    
    while compare > 0 :
        count = 0
        for i in citations :
            if i >= compare :
                count += 1
        if count >= compare :
            return compare
        compare -= 1
    return 0