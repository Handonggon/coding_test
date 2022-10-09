def solution(today, terms, privacies):
    answer = []

    today = today.split(".")
    for i in range(len(today)):
        today[i] = int(today[i])
    
    dict = {}
    for i in terms: #유효기간을 딕셔너리에 기록
        a = i.split(" ")
        dict[a[0]] = a[1]

    count = 0
    for i in privacies:
        count += 1
        a = i.split(".")
        y = int(a[0])
        m = int(a[1])
        d = int(a[2][:2])
        p = a[2][-1]
        
        today_y = (today[0] - y)*12
        today_m = today[1] - m
        today_d = today[2] - d

        today_ym = today_y + today_m


        if today_ym > int(dict[p]):
            answer.append(count)
        elif today_ym == int(dict[p]):
            if today_d >= 0:
                answer.append(count)
            else:
                pass
        else:
            pass
    return answer