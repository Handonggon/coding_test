def solution(id_list, report, k):
    
    report = set(report)
    dic = {} #이사람이 신고한 사람
    dic2 = {} #이사람이 얼마나 신고 당했는지
    dic3 = {} #신고한사람이 신고된 수
    reported = []
    for i in id_list:
        dic.setdefault(i,[])
        dic2.setdefault(i,0)
        dic3.setdefault(i,0)
    for j in dic:
        pass
    for i in report:
        a = i.split(" ")
        dic[a[0]].append(a[1])
        dic2[a[1]] += 1 # 신고 당한 사람
    for key in dic2:
        # print(dic2[key])
        if dic2[key] >= k :
            reported.append(key)
        else:
            pass
    for j in reported: # 사람 리스트
        for i in dic: # 신고접수 된사람
            if j in dic[i]:
                # print('정지된사람',j)
                # print("{}은".format(i))
                # print('이사람들 신고했어',dic[i])
                dic3[i] += 1

            else:
                pass
    return list(dic3.values())