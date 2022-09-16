def solution(n):
    answer = []
    list_n = [[i+1] for i in range(n)]
    fillnumber = n
    transnumber = 0
    linecount = n-1
    numcount = n
    direction = 1
    if n%2 == 0:
        stopnum = (1+n)*(n/2) -1
    else:
        stopnum = (((1+n)*(int(n/2))) + (1+n)/2) -1


    while stopnum != numcount-1:
        if list_n[linecount][0] == fillnumber:  #채우는 리스트에 도달하면
            while len(list_n[linecount]) != list_n[linecount][0]: #그 리스트의 길이와 첫번째 인덱스가 같아질때까지 카운트를 append해준다
                numcount += 1     
                list_n[linecount].append(numcount)    
                            
            transnumber += 2 #방향전환 리스트도 바꿔주기
            direction = -1 #움직이는 방향도 위로 바꿔준다

        elif list_n[linecount][0] == transnumber: #방향전환 해야하는 리스트에 도달하면
            if len(list_n[linecount]) != list_n[linecount][0]: #방향전환 리스트가 다채워지지 않았다면
                numcount += 1 #하나 채우고
                list_n[linecount].append(numcount)
                
            fillnumber -= 1 #방향전환하고 나서 채워야하는 리스트를 바꿔야 목표가 잘 설정된다
            direction = 1 #방향전환

        else: #채우는 리스트도아니고 방향전환할 필요도 없다면
            numcount += 1
            list_n[linecount].append(numcount)
            
        linecount += direction
    return answer
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
시간초과 너무 어렵게 푼건가 싶음
from collections import deque
def solution(n):
    answer = []
    list_n = [deque([i+1]) for i in range(n)]
    fillnumber = n
    transnumber = 0
    linecount = n-1
    numcount = n
    direction = 1
    headlistn = 0
    headlist = deque([])
    insertlist = deque([])
    talelistn = 0
    talelist = deque([])
    if n%2 == 0:
        stopnum = (1+n)*(n/2) -1
    else:
        stopnum = (((1+n)*(int(n/2))) + (1+n)/2) -1

    
    while stopnum != numcount-1:
        if list_n[linecount][0] == fillnumber:  #채우는 리스트에 도달하면
            if headlistn == 0:
                headlist.append(list_n[linecount].popleft())
            for i in range(headlistn):
                headlist.append(list_n[linecount].popleft())
            for i in range(talelistn):
                talelist.append(list_n[linecount].popleft())
            
            h = len(headlist)
            t = len(talelist)
            count = 0

            while h+count+t != fillnumber: #그 리스트의 길이와 첫번째 인덱스가 같아질때까지 카운트를 append해준다
                numcount += 1
                insertlist.append(numcount)
                count += 1
            while headlist != deque([]):
                insertlist.appendleft(headlist.pop())
            while talelist != deque([]):
                insertlist.append(talelist.popleft())
            list_n[linecount] = insertlist.copy()
            insertlist = deque([])
        

            headlistn += 1
            transnumber += 2 #방향전환 리스트도 바꿔주기
            direction = -1 #움직이는 방향도 위로 바꿔준다

        elif list_n[linecount][0] == transnumber: #방향전환 해야하는 리스트에 도달하면
            if len(list_n[linecount]) != list_n[linecount][0]: #방향전환 리스트가 다채워지지 않았다면
                numcount += 1 #하나 채우고

                for i in range(headlistn):
                    headlist.append(list_n[linecount].popleft())
                
                insertlist.append(numcount)
                
                for i in range(talelistn):
                    talelist.append(list_n[linecount].popleft())

                headlist.append(insertlist.pop())
                while talelist != deque([]):
                    headlist.append(talelist.popleft())
                list_n[linecount] = headlist.copy()
                headlist = deque([])
                
            talelistn += 1
            fillnumber -= 1 #방향전환하고 나서 채워야하는 리스트를 바꿔야 목표가 잘 설정된다
            direction = 1 #방향전환

        else: #채우는 리스트도아니고 방향전환할 필요도 없다면
            numcount += 1
            for i in range(headlistn):
                headlist.append(list_n[linecount].popleft())
            
            insertlist.append(numcount)

            for i in range(talelistn):
                talelist.append(list_n[linecount].popleft())
                

            headlist.append(insertlist.pop())
            while talelist != deque([]):
                headlist.append(talelist.popleft())
            list_n[linecount] = headlist.copy()
            
            headlist = deque([])

        linecount += direction
    
    for i in list_n:
        while i != deque([]):
            answer.append(i.popleft())

    return answer