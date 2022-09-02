def solution(bridge_length, weight, truck_weights):
    bridge = []
    finished = []
    bridge_time = []
    result = truck_weights[:]
    time = 0
    while finished != result :
        time += 1
        if bridge_length in bridge_time :
            finished.append(bridge.pop(0))
            bridge_time.pop(0)
        if len(bridge) < bridge_length and len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] <= weight :
                bridge.append(truck_weights.pop(0))
                bridge_time.append(0)    
        if len(bridge_time) > 0 :
            for i in range(len(bridge_time)) :
                bridge_time[i] += 1
        
    return time 