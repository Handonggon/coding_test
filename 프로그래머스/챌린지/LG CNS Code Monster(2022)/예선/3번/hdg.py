def solution(reference, track):
    combination = {}
    for start in range(len(reference)):
        for end in range(start+1, len(reference)+1):
            combination[reference[start:end]] = (end - start)

    answer = [len(track)]
    for i in range(len(track)):
        lenght = 1
        for j in range(i+1):
            if track[j:i+1] in combination:
                lenght = max(lenght, min(answer[j], combination[track[j:i+1]]))
        answer.append(lenght)
    return answer[-1]