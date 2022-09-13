def solution(record):
    dict = {}
    list_n = []
    answer = []
    for i in record:
        a = i.split(" ")
        dict[a[1]] = []
    for i in record:
        a = i.split(" ")
        if a[0] != "Leave":
            dict[a[1]].append(a[2])
        else:
            pass
    string = ""
    for i in record:
        a = i.split(" ")
        if a[0] == "Enter":
            string += dict[a[1]][-1]
            string += "님이 들어왔습니다."
            answer.append(string)
            string = ""
        elif a[0] == "Leave":
            string += dict[a[1]][-1]
            string += "님이 나갔습니다."
            answer.append(string)
            string = ""
        else:
            pass
    return answer