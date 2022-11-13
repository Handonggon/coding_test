def solution(k, limits, sockets):
    global answer
    answer = 0

    def dfs(node):
        count = 0
        for type in sockets[node]:
            if type == 0 :
                continue

            if type == -1:
                count += 1
            else :
                count += dfs(type-1)

        limit = limits[node] // k
        if count > limit:
            global answer
            answer += (count - limit)
        return min(limit, count)

    dfs(0)
    return answer