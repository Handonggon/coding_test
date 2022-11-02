from collections import deque
import math
import sys
input = sys.stdin.readline

# 세그먼트 트리
N = int(input())
info = sorted(list(map(lambda x: [x[0], int(x[1])], enumerate(input().split()))), key=lambda x: x[1])

#N = 8
#info = sorted(list(map(lambda x: [x[0], int(x[1])], enumerate([8, 2, 7, 6, 4, 5, 1, 3]))), key=lambda x: x[1])
#N = 3
#info = sorted(list(map(lambda x: [x[0], int(x[1])], enumerate([3, 2, 1]))), key=lambda x: x[1])

tree = [0] * (2 << math.ceil(math.log2(N)))

def init(start, end, node):
    tree[node] = (1 if start == end else init(start, (start+end)//2, node*2) + init(((start+end)//2)+1, end, node*2+1))
    return tree[node]

def query(start, end, left, right, node):
    if (right < start or left > end):
        return 0
    if (left <= start and end <= right):
        return tree[node]
    return query(start, (start+end)//2, left, right, node*2) + query(((start+end)//2)+1, end, left, right, node*2+1)

def update(start, end, idx, node, value):
    if (start <= idx and end >= idx):
        if (start == end):
            if(start == idx):
                tree[node] = value
        else:
            update(start, (start+end)//2, idx, node*2, value)
            update(((start+end)//2)+1, end, idx, node*2+1, value)
            tree[node] = tree[node*2] + tree[node*2+1]

init(0, N-1, 1)

answer = 0
for i in range(N):
    [q, _] = info[i]
    answer += query(0, N-1, 0, q, 1) - 1
    update(0, N-1, q, 1, 0)
print(answer)

# 합병정렬
N = int(input())
info = list(map(int, input().split()))

#N = 8
#info = [8, 2, 7, 6, 4, 5, 1, 3]
#N = 3
#info = [3, 2, 1]

def merge(left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    answer = merge(left, mid) + merge(mid+1, right)
    queue = deque([])
    [i, j] = [left, mid+1]

    while (i <= mid or j <= right):
        if i <= mid and (j > right or info[i] <= info[j]):
            queue.append(info[i])
            i += 1
        else:
            queue.append(info[j])
            j += 1
            answer += mid - i + 1

    for i in range(left, right+1):
        info[i] = queue.popleft()

    return answer

print(merge(0, N-1))