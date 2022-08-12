def solution(n):
    
    total = 1
    for i in range(1, (n//2)+1):
        answer = 0
        
        while answer < n:
            answer += i
            i += 1
            
        if answer == n:
            total += 1
            
    return total