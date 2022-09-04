def solution(n):
    result =[]
    dic_hanoi = {0 : [i for i in range(1,n+2)], 1 : [n+1], 2: [n+1]}
    
    while len(dic_hanoi[2]) - 1 != n :
        i = 0
        while i < 3 :
            if len(dic_hanoi[2]) - 1 == n :
                break
            elif min(dic_hanoi[i]) < min(dic_hanoi[(i+1)%3]) or min(dic_hanoi[i]) < min(dic_hanoi[(i+2)%3]) :
                k = (i+1+((len(dic_hanoi[i])-1)%2))%3 + (((-1)**(((len(dic_hanoi[i])-1)%2)+1))*2*(i%2))
                if min(dic_hanoi[i]) < min(dic_hanoi[k]) :
                    result.append([i+1,k+1])
                    dic_hanoi[k].insert(0,dic_hanoi[i].pop(0))
                else :
                    i +=1
            else :
                i += 1
    return result