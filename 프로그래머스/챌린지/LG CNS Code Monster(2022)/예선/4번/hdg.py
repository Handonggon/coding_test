def solution(edges, roots):
    n = max(map(lambda x: max(x), edges))
    print(n)

    graph = [[-1 for _ in range(n)] for _ in range(n)]
    for index in range(len(edges)):
        v, w = edges[index]
        graph[v-1][w-1] = index

    answer = [0] * len(edges)
    for root in roots:
        stack = [root-1]
        visited = [False for _ in range(n)]

        while stack:
            curr = stack.pop()
            visited[curr] = True

            for node in range(n):
                if not visited[node]:
                    if graph[node][curr] > -1:
                        index = graph[node][curr]
                        graph[curr][node] = index
                        graph[node][curr] = -1
                        answer[index] += 1

            for next in range(n):
                if graph[curr][next] > -1:
                    stack.append(next)

    return answer