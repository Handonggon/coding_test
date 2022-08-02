def block(n):
    if n == 1:
        return 0
    for i in range(2,10000000):
        if n < i:
            break
        mo,na = divmod(n,i)
        if n != i and na ==0:
            return mo
    return 1
def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer
테스트 1 〉	통과 (19.33ms, 10.1MB)
테스트 2 〉	통과 (78.17ms, 10.3MB)
테스트 3 〉	통과 (40.24ms, 10.2MB)
테스트 4 〉	통과 (54.55ms, 10.1MB)
테스트 5 〉	통과 (52.29ms, 10.2MB)
테스트 6 〉	통과 (7.98ms, 10.4MB)
테스트 7 〉	통과 (98.47ms, 10.2MB)
테스트 8 〉	통과 (17.55ms, 10.1MB)
테스트 9 〉	통과 (38.28ms, 10.2MB)
테스트 10 〉통과 (113.47ms, 10.3MB)
테스트 11 〉통과 (44.66ms, 10.1MB)
테스트 12 〉통과 (11.32ms, 10.2MB)
테스트 13 〉통과 (0.11ms, 10.3MB)
테스트 14 〉통과 (27.94ms, 10.1MB)
#효율성 테스트 실패
def block(n):
    if n == 1:
        return 0
    for i in range(2,10000000):
        if n < i:
            break
        mo = n//i
        na = n%i
        if n != i and na ==0:
            return mo
    return 1
def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer
테스트 1 〉	통과 (13.08ms, 10MB)
테스트 2 〉	통과 (67.07ms, 10.1MB)
테스트 3 〉	통과 (45.80ms, 10MB)
테스트 4 〉	통과 (29.42ms, 10MB)
테스트 5 〉	통과 (35.18ms, 10.2MB)
테스트 6 〉	통과 (4.09ms, 9.93MB)
테스트 7 〉	통과 (59.23ms, 10.2MB)
테스트 8 〉	통과 (7.85ms, 9.96MB)
테스트 9 〉	통과 (22.48ms, 10.2MB)
테스트 10 〉통과 (123.79ms, 10.2MB)
테스트 11 〉통과 (27.58ms, 10.1MB)
테스트 12 〉통과 (8.45ms, 10.1MB)
테스트 13 〉통과 (0.08ms, 10.2MB)
테스트 14 〉통과 (19.24ms, 10.1MB)

def block(n):
    if n == 1:
        return 0
    for i in range(2,10000000):
        if n < i:
            break
        if n%i != 0:
            continue
        else:
            mo = n//i
            na = n%i
            if n != i and na ==0:
                return mo
    return 1
def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer

테스트 1 〉	통과 (8.34ms, 10.2MB)
테스트 2 〉	통과 (37.95ms, 10.2MB)
테스트 3 〉	통과 (20.22ms, 10.3MB)
테스트 4 〉	통과 (28.21ms, 9.95MB)
테스트 5 〉	통과 (20.96ms, 10.2MB)
테스트 6 〉	통과 (2.67ms, 10.1MB)
테스트 7 〉	통과 (38.53ms, 10.3MB)
테스트 8 〉	통과 (5.34ms, 10.2MB)
테스트 9 〉	통과 (14.46ms, 10.1MB)
테스트 10 〉통과 (52.04ms, 10.2MB)
테스트 11 〉통과 (17.71ms, 10.1MB)
테스트 12 〉통과 (5.47ms, 9.92MB)
테스트 13 〉통과 (0.05ms, 10.2MB)
테스트 14 〉통과 (12.00ms, 10.2MB)




list_h = list(range(3,10000000,2))
def block(n):
    if n < 20000000: 
        if n == 1:
            return 0
        for i in range(2,10000000):
            if n < i:
                break
            if n%i != 0:
                continue
            else:
                mo = n//i
                na = n%i
                if n != i and na ==0:
                    return mo
        return 1
    else:
        if n%2 ==0:
            return 10000000
        else:
            for i in list_h:
                if n%i != 0:
                    continue
                else:
                    mo = n//i
                    return mo
            return 1

def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer

테스트 1 〉	통과 (13.91ms, 203MB)
테스트 2 〉	통과 (41.88ms, 203MB)
테스트 3 〉	통과 (24.07ms, 203MB)
테스트 4 〉	통과 (19.47ms, 203MB)
테스트 5 〉	통과 (19.17ms, 203MB)
테스트 6 〉	통과 (2.65ms, 203MB)
테스트 7 〉	통과 (51.47ms, 203MB)
테스트 8 〉	통과 (4.98ms, 203MB)
테스트 9 〉	통과 (16.60ms, 203MB)
테스트 10 〉	통과 (79.62ms, 203MB)
테스트 11 〉	통과 (25.41ms, 203MB)
테스트 12 〉	통과 (5.74ms, 203MB)
테스트 13 〉	통과 (0.06ms, 203MB)
테스트 14 〉	통과 (11.91ms, 203MB)


list_h = list(range(3,10000000,2))
def block(n):
    if n < 20000000: 
        if n == 1:
            return 0
        for i in range(2,(n//2)+3):
            if n < i:
                break
            if n%i != 0:
                continue
            else:
                mo = n//i
                na = n%i
                if n != i and na ==0:
                    return mo
        return 1
    else:
        if n%2 ==0:
            return 10000000
        else:
            for i in list_h:
                if n%i != 0:
                    continue
                else:
                    mo = n//i
                    return mo
            return 1

def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer

테스트 1 〉	통과 (4.17ms, 203MB)
테스트 2 〉	통과 (18.57ms, 203MB)
테스트 3 〉	통과 (13.58ms, 203MB)
테스트 4 〉	통과 (9.95ms, 203MB)
테스트 5 〉	통과 (9.59ms, 203MB)
테스트 6 〉	통과 (2.32ms, 203MB)
테스트 7 〉	통과 (19.07ms, 203MB)
테스트 8 〉	통과 (2.48ms, 203MB)
테스트 9 〉	통과 (13.25ms, 203MB)
테스트 10 〉	통과 (24.77ms, 203MB)
테스트 11 〉	통과 (16.74ms, 203MB)
테스트 12 〉	통과 (5.28ms, 203MB)
테스트 13 〉	통과 (0.06ms, 203MB)
테스트 14 〉	통과 (6.00ms, 203MB)
------------------------------------------------------