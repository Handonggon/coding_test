시간초과 
def solution(numbers):
    answer = []
    for n in numbers:
        target = n
        tbit = ""
        while target != 0:
            tbit += str(target%2)
            target = target//2

        count = n+1
        while count!= (10**15)+1:
            i = count
            cbit = ""
            while i != 0:
                cbit += str(i%2)
                i = i//2
            
            a = 0
            possible = True
            for j in range(len(cbit)):
                if len(tbit) > j:
                    if cbit[j] == tbit[j]:
                        pass
                    else:
                        a += 1
                else:
                    for m in cbit[j:]:
                        if m == "0":
                            pass
                        else:
                            a += 1
                if a > 2:
                    possible =False
                    break
            if possible == True:
                answer.append(count)
                break
            else:
                count += 1
    return answer