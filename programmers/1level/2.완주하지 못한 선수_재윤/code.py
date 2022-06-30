def solution(participant, completion):
    answer = ""
    for i in completion:
        participant.remove(i)  
    for i in participant:
        if participant[:-1]:
            answer += i + ','
        elif participant[-1]:
            answer += i    
        
    return answer