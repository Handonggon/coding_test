def solution(msg):
    numd = 27
    result = []
    dictionary = {chr(i) : i-64 for i in range(65,91)}
    
    i = 0
    while i < len(msg) :
        temp = msg[i]
        k = i + 1
        temp2 = temp
        while k < len(msg) and temp in dictionary.keys() :
            temp2 = temp
            temp += msg[k]
            i = k - 1
            k += 1
        if temp in dictionary.keys() :
            result.append(dictionary[temp])
            break
        else :
            result.append(dictionary[temp2])
            dictionary[temp] = numd
            numd += 1
        i += 1

    return result