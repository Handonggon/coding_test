def solution(a,b):
    answer = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        answer += a[0]*b[-1]
        a.pop(0)
        b.pop(-1)
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer