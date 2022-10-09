import math

def stob(s) :
    sb = s.split(':') 
    return 60*int(sb[0]) + int(sb[1])

def solution(fees, records):
    dic_record = {}
    for car in records :
        car_list = car.split(' ')
        if car_list[2] == "IN" :
            if car_list[1] in dic_record.keys() :
                dic_record[car_list[1]].append(car_list[0])
            else :
                dic_record[car_list[1]] = [car_list[0]]
        else :
            dic_record[car_list[1]].append(car_list[0])
    
    dic_record = dict(sorted(dic_record.items()))
    result = []
    for value in dic_record.values() :
        sum = 0
        idx = 0
        while idx < len(value) :
            try :
                sum += stob(value[idx+1]) - stob(value[idx])
                idx += 2
            except :
                sum += 1439 - stob(value[idx])
                break
        result.append(sum)
    
    print(result)
    for i in range(len(result)) :
        if result[i] > fees[0] :
            result[i] = fees[1] + math.ceil((result[i]-fees[0])/fees[2]) *fees[3]
        else :
            result[i] = fees[1]
    
    return result
    