import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    # init    
    h = [0 for _ in range(n + n)]
    for i in range(n - 1, 0, -1):
        h[i] = h[i + i] + 1
    lenght = n + 1
    cnt = [0 for _ in range(n + n + 1)]
    cnt[1] += 1
    cnt[2] += 1

    w = [1] + [0 for _ in range(n)]
    a = [1] + [0 for _ in range(n)]


    def dfs(idx, mx):
        global lenght
        if idx + h[w[idx - 1]] >= lenght:
            return

        if w[idx-1] == n:
            lenght = idx
            for i in range(lenght):
                a[i] = w[i]
            return

        for i in range(min(n, mx), w[idx-1], -1):
            if not cnt[i]:
                continue
            w[idx] = i;
            for j in range(idx + 1):
                cnt[w[j] + i] += 1
            dfs(idx + 1, 2 * i);
            for j in range(idx + 1):
                cnt[w[j] + i] -= 1

    dfs(1, 2)
    print(a[:lenght])