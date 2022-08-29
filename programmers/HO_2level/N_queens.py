n = 5

stack = []
res = 0
for a in range(n):
    for b in range(n):
        z = []
        rect = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        rect[a][b] = 1
        for c in range(n):
            rect[a][c] = 1
        for c in range(n):
            rect[c][b] = 1
        for c in range(n):
            if 0<=a+c <= n-1 and 0<=b+c <= n-1:
                rect[a+c][b+c] = 1
            if 0<=a-c <= n-1 and 0<=b-c <= n-1:
                rect[a-c][b-c] = 1
            if 0<=a-c <= n-1 and 0<=b+c <= n-1:
                rect[a-c][b+c] = 1
            if 0<=a+c <= n-1 and 0<=b-c <= n-1:
                rect[a+c][b-c] = 1    
        z.append((a,b))           
        
        for i in range(n):
            for j in range(n):
                if rect[i][j] == 0:
                    for k in range(n):
                        rect[i][k] = 1
                    for k in range(n):
                        rect[k][j] = 1
                    for k in range(n):
                        if 0<=i+k <= n-1 and 0<=j+k <= n-1:
                            rect[i+k][j+k] = 1
                        if 0<=i-k <= n-1 and 0<=j-k <= n-1:
                            rect[i-k][j-k] = 1
                        if 0<=i-k <= n-1 and 0<=j+k <= n-1:
                            rect[i-k][j+k] = 1
                        if 0<=i+k <= n-1 and 0<=j-k <= n-1:
                            rect[i+k][j-k] = 1
                    cnt += 1
                    z.append((i,j))
        z.sort()
        if cnt == n and z not in stack:
            stack.append(z)
            res += 1 
print(stack)
print(res)