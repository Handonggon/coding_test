def solution(str1, str2):
    str1_arr = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].lower().isalpha()]
    str2_arr = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].lower().isalpha()]

    union, intersection = 0, 0
    for element in set(str1_arr + str2_arr):
        union += max(str1_arr.count(element), str2_arr.count(element))
        intersection += min(str1_arr.count(element), str2_arr.count(element))

    return 65536 if union == 0 else int((intersection / union) * 65536)

#테스트 1 〉	통과 (0.03ms, 10.4MB)
#테스트 2 〉	통과 (0.04ms, 10.3MB)
#테스트 3 〉	통과 (0.02ms, 10.2MB)
#테스트 4 〉	통과 (7.30ms, 10.5MB)
#테스트 5 〉	통과 (0.04ms, 10.3MB)
#테스트 6 〉	통과 (0.02ms, 10MB)
#테스트 7 〉	통과 (0.52ms, 10.2MB)
#테스트 8 〉	통과 (0.02ms, 10.2MB)
#테스트 9 〉	통과 (0.23ms, 10.3MB)
#테스트 10 〉	통과 (0.65ms, 10.3MB)
#테스트 11 〉	통과 (3.19ms, 10.2MB)
#테스트 12 〉	통과 (0.01ms, 10.2MB)
#테스트 13 〉	통과 (0.13ms, 10.1MB)

#===================================================================================================================================#

def solution(str1, str2):
    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]
    
    dict1 = {}
    for word in list1:
        dict1[word] = dict1.get(word, 0) + 1
        
    dict2 = {}
    for word in list2:
        dict2[word] = dict2.get(word, 0) + 1
    
    union, intersection = 0, 0
    for word in set(list1 + list2):
        union += max(dict1.get(word, 0), dict2.get(word, 0))
        intersection += min(dict1.get(word, 0), dict2.get(word, 0))
    
    return 65536 if union == 0 else int((intersection / union) * 65536)

#테스트 1 〉	통과 (0.02ms, 10.2MB)
#테스트 2 〉	통과 (0.03ms, 10.3MB)
#테스트 3 〉	통과 (0.02ms, 10.2MB)
#테스트 4 〉	통과 (0.80ms, 10.3MB)
#테스트 5 〉	통과 (0.03ms, 10.2MB)
#테스트 6 〉	통과 (0.02ms, 10.2MB)
#테스트 7 〉	통과 (0.10ms, 10.2MB)
#테스트 8 〉	통과 (0.02ms, 10.2MB)
#테스트 9 〉	통과 (0.10ms, 10.2MB)
#테스트 10 〉	통과 (0.15ms, 10.2MB)
#테스트 11 〉	통과 (0.25ms, 10.2MB)
#테스트 12 〉	통과 (0.01ms, 10.2MB)
#테스트 13 〉	통과 (0.06ms, 10.2MB)
