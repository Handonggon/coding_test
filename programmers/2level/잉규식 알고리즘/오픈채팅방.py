def solution(record):
    log_list = []
    for i in record :
        log_list.append(i.split(' '))
    dic_user = {}
    result = []
    for log in log_list :
        if log[0] == 'Enter' :
            if log[1] not in dic_user.keys() :
                dic_user[log[1]] = []
            dic_user[log[1]].append(log[2])
        elif log[0] == 'Change' :
            dic_user[log[1]].append(log[2])
    for log in log_list :
        if log[0] == 'Enter' :
            result.append(dic_user[log[1]][-1]+"님이 들어왔습니다.")
        elif log[0] == 'Leave' :
            result.append(dic_user[log[1]][-1]+"님이 나갔습니다.")
    
    return result