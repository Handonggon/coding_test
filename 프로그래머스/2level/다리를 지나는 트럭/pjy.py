from collections import deque
def solution(length, weight, truck):
    arrive = []
    des = truck
    bridge = deque()
    truck = deque(truck)
    count = 0
    now = 0
    while arrive != des:
        count += 1
        if len(bridge) > 0 :
            a = bridge.popleft()
            if count - a[1] == length:
                arrive.append(a[0])
                now -= a[0]
            else:
                bridge.appendleft(a)
        else:
            pass
        if len(truck) > 0 :
            b = truck.popleft()
            if b + now > weight:
                truck.appendleft(b)
            else:
                bridge.append([b,count])
                now += b
        else:
            pass
    return count