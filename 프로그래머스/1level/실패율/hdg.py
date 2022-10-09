def solution(N, stages):
    situation = [0 for i in range(N+1)]
    for stage in stages:
        situation[stage-1] += 1

    answer = {}
    arrival = len(stages)
    for level, count in enumerate(situation[:N]):
        try:
            answer[level+1] = count/arrival
        except:
            answer[level+1] = 0
        arrival -= count

    return sorted(answer, key=answer.get, reverse=True)
