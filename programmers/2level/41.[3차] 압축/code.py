from collections import deque
def solution(msg):
    dict = {}
    answer = []
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(a)):
        dict[a[i]] = i+1
    list_w = deque([])
    string = ''
    for i in msg:
        list_w.append(i)
    while list_w != deque([]):
        string += list_w.popleft()
        if string in dict:
            continue
        else:
            a = len(dict)
            dict[string] = a+1
            answer.append(dict[string[:len(string)-1]])
            string = string[-1]
    answer.append(dict[string])
    return answer