런타임에러 아마 출력크기가 넘어가서 생긴 오류인듯
def solution(n, times):
    answer = 0
    tm = 1
    for i in times: #일이 같이 끝나는 시간 찾기
        tm *= i
        while tm%2 == 0: #최소공배수 찾기
            tm = int(tm/2)
    work = []
    for i in times: #일이 같이 끝날때 얼마나 처리했는지
        work.append(int(tm/i))
    tmw = sum(work)
    # while tmw > n : #이분탐색은 이것 같은데
    #     tmw *= 1/2
    #     tm *= 1/2 
    notrefined = int(tm * (n/tmw)) #정제되지 않은 리턴값 이걸찾는게 더 낫다고 생각

    almost = [] #일이 끝나갈때즈음이랑 가장 가까운 일처리 상황
    com = 0 # 그때쯤 몇명을 처리했는지
    for i in times: 
        a = int(notrefined/i)
        almost.append(i*a)
        com += a
    if com == n: #만약 가장가까울때 일처리가 끝났다면 끝난 시간을 리턴하고
        return(max(almost))
    else: #그게아니라면 가장 일처리가 빠른사람한테 일을 시켜서 빠르게 끝낸다
        for i in range(len(almost)):
            almost[i] += times[i]
        return(min(almost))
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
풀이 오류인듯

def solution(n, times):
    if n-len(times) <= 0: # 대기인원보다 심사관이 더 많거나 인원이 같다면
        times.sort()
        return times[n-len(times)-1]
    answer = 0
    tm = 1
    for i in times: #일이 같이 끝나는 시간 찾기
        tm *= i
        while tm%2 == 0:
            tm = int(tm/2)
    work = []
    for i in times: #일이 같이 끝날때 얼마나 처리했는지
        work.append(int(tm/i))
    tmw = sum(work)
    # while tmw > n : #이분탐색은 이것 같은데
    #     tmw *= 1/2
    #     tm *= 1/2 
    notrefined = int(tm * (n/tmw)) #정제되지 않은 리턴값 이걸찾는게 더 낫다고 생각
    almost = [] #일이 끝나갈때즈음이랑 가장 가까운 일처리 상황
    com = 0 # 그때쯤 몇명을 처리했는지
    overload = [] # 일안하는 있는사람 있는지 
    
    for i in times: 
        a = int(notrefined/i)
        overload.append(a)
        almost.append(i*a)
        com += a
    if 0 in overload : #일 안하게된 사람이 있다면
        return max(times)

    if com == n: #만약 가장가까울때 일처리가 끝났다면 끝난 시간을 리턴하고
        return(max(almost))
    else: #그게아니라면 가장 일처리가 빠른사람한테 일을 시켜서 빠르게 끝낸다
        for i in range(len(almost)):
            almost[i] += times[i]
        return(min(almost))
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#이분탐색 1차 실패
def solution(n, times):
    time  = [0,10000000000000000000] # 최대치
    while time != [0,0]:
        if time[0] == time[1]:
            return time[0]
        count = 0 
        a = time[0] + ((time[1]-time[0])//2)
        for i in times:
            count += int(a/i)
        if count > n:
            time[1] -= ((time[1]-time[0])//2) +1
        elif count < n:
            time[0] += ((time[1]-time[0])//2) +1
        else:
            if time[1]-time[0] < 10:
                time[1] -= ((time[1]-time[0])//2) +1
            else:
                count = 0
                while time[1]-time[0] != 0:
                    for i in times:
                        count += time[0]
                    if count == n:
                        return time[0]
                    else:
                        time[0] += 1
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
2차 성공
def solution(n, times):
    time  = [0,100000000000000000000] # 최대치
    while time != [0,0]:
        if time[0] == time[1]:
            return time[0]
        count = 0 
        a = time[0] + ((time[1]-time[0])//2)
        for i in times:
            count += int(a/i)
        if count > n:
            time[1] -= ((time[1]-time[0])//2) +1
        elif count < n:
            time[0] += ((time[1]-time[0])//2) +1
        else:
            if time[1]-time[0] > 10:
                time[1] -= ((time[1]-time[0])//2) +1
            else:
                while time[1]-time[0] != 0:
                    count = 0
                    for i in times:
                        count += int(time[0]/i)
                    if count == n:
                        return time[0]
                    else:
                        time[0] += 1