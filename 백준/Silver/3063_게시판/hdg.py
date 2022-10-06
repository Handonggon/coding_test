T = int(input())

for _ in range(T):
    [x1, y1, x2, y2, x3, y3, x4, y4] = list(map(int, input().split()))
    
    poster = (x2 - x1) * (y2 - y1)
    x = (min(x2, x4) - max(x1, x3))
    y = (min(y2, y4) - max(y1, y3))
    if x < 0 or y < 0:
        print(poster)
    else:
        print(poster - (x * y))
