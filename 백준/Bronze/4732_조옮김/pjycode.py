list_m = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
while True:
    m = input().split(" ")
    if m ==["***"]:
        break
    plus = int(input())
    nm = []
    for i in m:
        a = ""
        if i not in list_m:
            count = list_m.index(i[0])
            if i[1] == "#":
                a += list_m[count+1]
            else:
                a += list_m[count-1]
        else:
            a += i
        nm.append(a)
    answer = []
    for i in nm:
        count = list_m.index(i)
        count = count + plus
        answer.append(list_m[count%12])
    f = ""
    for i in answer:
        f += i
        f += " "
    print(f[:-1])