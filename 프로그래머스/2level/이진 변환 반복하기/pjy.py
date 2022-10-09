def solution(s):
    answer = [0,0]
    list_n = []
    for i in s: #s를 리스트화
        list_n.append(int(i))

    while list_n != [1]:
        answer[0] += 1
        count = 0
        while len(list_n)>count:
            if list_n[count] == 0:
                list_n.pop(count)
                answer[1] += 1
            else:
                count += 1
        if list_n != [1]:
            n = len(list_n)
            list_n= []
            while n!= 0:    
                list_n.append(n%2)
                n = n//2
                list_n = list_n[::-1]
        else:
            return answer