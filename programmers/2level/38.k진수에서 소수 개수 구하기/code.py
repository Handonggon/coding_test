def solution(n, k):
    nary = ""
    while n != 0:
        nary += str(n % k)
        n = n//k 
    nary = nary[-1::-1]
    list_n = []
    number = ""
    for i in range(len(nary)):
        if nary[i] != '0':
            number += nary[i]
        else:
            if len(number) > 0:
                if number != "1":
                    list_n.append(int(number))
                number = ""
            else:
                pass
        if i == len(nary)-1:
            if len(number) > 0 and number != "1":
                list_n.append(int(number))
    answer = 0
    prime = True
    for i in list_n:
        if i == 2 or i == 3:
            answer += 1
            continue
        for j in range(2,int(i**(1/2))+2):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            answer += 1
        else:
            prime = True
    return answer