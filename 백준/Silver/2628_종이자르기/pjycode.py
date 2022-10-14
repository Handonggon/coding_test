g,s = input().split(" ")
count = int(input())
list_n = [['0' for j in range(int(g))] for i in range(int(s))]
while count != 0:
    a,b = input().split(" ")
    if a == "0": #가로로 자를때
        for i in range(int(b)):
            for j in range(len(list_n[i])):
                list_n[i][j] += str(count)
    else:       #세로로 자를떄
        for i in range(len(list_n)):
            for j in range(int(b)):
                list_n[i][j] += str(count)
    count -= 1
dict = {}
for i in range(len(list_n)):
    for j in range(len(list_n[i])):
        dict[list_n[i][j]] = 0
for i in range(len(list_n)):
    for j in range(len(list_n[i])):
        dict[list_n[i][j]] += 1
print(max(dict.values()))