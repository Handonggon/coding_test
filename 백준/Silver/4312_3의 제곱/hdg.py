import sys
input = sys.stdin.readline

while True:
    n = int(input()) - 1
    if n == -1:
        break

    answer = []
    index = 0
    while n > 0:
        if n % 2:
            answer.append(index)
        n = n // 2
        index += 1

    print("{", ",".join(map(lambda i: " " + str(pow(3, i)), answer)), " }", sep = "")