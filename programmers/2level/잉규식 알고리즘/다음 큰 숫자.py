def solution(n):
    list_n = [i for i in bin(n)][2:]
    change = False
    for index in range(len(list_n)-2,-1,-1) :
        if list_n[index] < list_n[index+1] :
            temp = list_n[index]
            list_n[index] = list_n[index+1]
            list_n[index+1] = temp
            change = True
            break
    if change :
        list_n = list_n[:index+1] + sorted(list_n[index+1:])
    else :
        list_n.insert(1,'0')
        list_n = [list_n[0]] + sorted(list_n[1:])
    result = ''.join(map(str,(['0','b']+list_n)))
    
    return int(result,2)