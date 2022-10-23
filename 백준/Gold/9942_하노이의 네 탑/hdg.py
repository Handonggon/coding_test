case = 0
while True:
    case += 1
    try :
        N = int(input())

        answer = 0
        level = 1

        while N > 0:
            for _ in range(min(level, N)):
                answer += pow(2, level-1)
                N -= 1
            level += 1

        print(f'Case {case}: {answer}')
    except EOFError:
        break