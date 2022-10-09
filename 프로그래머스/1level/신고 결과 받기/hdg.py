def solution(id_list, reports, k):
    user_info = {}
    for user in id_list:
        user_info[user] = {}
        user_info[user]['report_user'] = set()
        user_info[user]['count'] = 0

    for report in reports:
        [report_id, use_id] = report.split(" ");
        user_info[use_id]['report_user'].add(report_id)

    for user in user_info.keys():
        if(len(user_info[user]['report_user']) >= k):
            for report_user in user_info[user]['report_user']:
                user_info[report_user]['count'] += 1

    return list(map(lambda _user: user_info[_user]['count'], id_list))
