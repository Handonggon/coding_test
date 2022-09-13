from collections import deque
def solution(fees, records):
    car_fee = {}
    car_record = {}
    for i in records:
        a = i.split(" ")
        car_fee[a[1]] = 0 #차량 별 요금부과
        car_record[a[1]] = deque([]) # 차량 별 출퇴 
    for i in records:
        a = i.split(" ")
        car_record[a[1]].append(a[0])
    for i in car_record:
        while car_record[i] != deque([]):
            if 2 <= len(car_record[i]):
                a = car_record[i].popleft()
                b = car_record[i].popleft()
            else:
                a = car_record[i].popleft()
                b = "23:59"
            h = (int(b[0:2]) - int(a[0:2]))*60
            m = int(b[3:]) - int(a[3:])
            time =  h+m
            car_fee[i] += time
    answer = []
    for i in sorted(car_fee,key = lambda x : int(x)):
        total = car_fee[i]
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            total -= fees[0]
            if total % fees[2] == 0:
                answer.append(((int(total/fees[2]))*fees[3])+fees[1])
            else:
                answer.append((((int(total/fees[2]))+1)*fees[3])+fees[1])
    return answer