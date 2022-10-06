ALPHABET = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def location(r, c):
    return ALPHABET[(c) // 26] + ALPHABET[(c) % 26 + 1] + str(r+1)

[R, C] = list(map(int, input().split()))
sheet = [input().split(" ") for _ in range(R)]

info = {}
for r in range(R):  
    for c in range(C):
        if sheet[r][c] == '.':
            info[location(r, c)] = []
        else:
            info[location(r, c)] = sheet[r][c].split("+")

global cycle
cycle = 'no'

stack = list(info.keys())

visited = {cell:False for cell in info.keys()}
finished = {cell:False for cell in info.keys()}

def dfs(curr):
    global cycle
    if cycle == 'yes':
        return

    visited[curr] = True

    for next in info[curr]:
        if not visited[next]:
            dfs(next)
        elif not finished[next]:
            cycle = 'yes'

    finished[curr] = True

for cell in info.keys():
    dfs(cell)

print(cycle)