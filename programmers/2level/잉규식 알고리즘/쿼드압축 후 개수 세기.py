top = [0,0]

def solution(arr) :
    tf = True
    for i in range(len(arr)-1) :
        if arr[i] == arr[i+1] and len(set(arr[i])) == 1:
            continue
        else :
            tf = False
            break
    
    if tf :
        result = [[arr[0][0]]]
    else :
        result = [[],[],[],[]]
        point = len(arr)//2

        for sarr in range(0,point) :
            result[0] += arr[sarr][:point]
            result[1] += arr[sarr][point:]
        for sarr in range(point,len(arr)) :
            result[2] += arr[sarr][:point]
            result[3] += arr[sarr][point:]

    for i in range(len(result)) :
        if len(set(result[i])) == 1 :   
            if list(set(result[i])) == [1] :
                top[1] += 1
            else :
                top[0] += 1
        else :
            if len(result[i]) == 4 :
                for j in range(len(result[i])) :
                    if result[i][j] == 1 :
                        top[1] += 1
                    else :
                        top[0] += 1
            else :
                temp = []
                for j in range(point):
                    temp.append(result[i][j*(len(result[i])//point):(j+1)*(len(result[i])//point)])
                solution(temp)
                
    return top