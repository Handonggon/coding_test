def solution(ingredient):
    a = ingredient
    count = 0
    n = 0
    while n < (len(a)//4+1):
        for i in range(len(a)-3):
            if a[i] == 1 and a[i+1] == 2 and a[i+2] == 3 and a[i+3] == 1:
                count += 1
            
                for j in range(4):
                    a.pop(i)
                break
        
        n += 1

    return count