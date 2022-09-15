from itertools import combinations

def solution(order, course):
    orders = []
    for i in order:
        sort_str = ''
        for j in i:
            sort_str += str(j)
        orders.append(sorted(sort_str))
    
    ans = []
    for i in course:
        box = []
        for j in orders:
            cnt_box = []
            for k in j:
                cnt_box.append(k)
            box.append(list(combinations(cnt_box, i)))
        
        dic = {}
        for j in box:
            for k in j:
                str_ = ''
                for l in k:
                    str_ += l
                if str_ not in dic: dic[str_] = 1
                else: dic[str_] += 1
        
        value = dic.values()

        if len(value) != 0:
            a = max(value)
            
            if a == 1:continue
            else:
                for key, value in dic.items():
                    if value == a:
                        ans.append(key)
    return sorted(ans)