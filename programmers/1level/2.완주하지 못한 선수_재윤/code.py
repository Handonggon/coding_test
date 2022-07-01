def solution(participant, completion):
    
    dict = {}
    dict = dict.fromkeys(participant,0)
    for i in participant:
        dict[i] += 1
    for people in completion:
        dict[people] -= 1
    answer = [k for k, v in dict.items() if v == 1]
    answer = ",".join(answer)
    

    return answer