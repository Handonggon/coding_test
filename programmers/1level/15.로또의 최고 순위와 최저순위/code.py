def solution(lottos, win_nums):
    exact=0
    perhaps=0
    for i in lottos:
        if i !=0:
            if i in win_nums:
                exact+=1
            else:
                pass
        else:
            perhaps+=1
    rank=[6,6,5,4,3,2,1]
    return [rank[exact+perhaps],rank[exact]]
            