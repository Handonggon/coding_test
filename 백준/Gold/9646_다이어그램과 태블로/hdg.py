import sys
input = sys.stdin.readline

while True:
    try:
        [k, info] = map(int, input().split())
        N = int(input())

        print(k, info, N)

        
    except EOFError:
        break