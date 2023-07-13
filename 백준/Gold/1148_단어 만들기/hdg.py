import sys
input = sys.stdin.readline

[MIN, MAX] = [0, 1]
words = []
while True:
    s = input().strip()
    if s == '-':
        break
    word = [0 for _ in range(26)]
    for c in s:
        word[ord(c) - 65] += 1
    words.append(word)

while True:
    s = input().strip()
    if s == '#':
        break
    board = [0 for _ in range(26)]
    for c in s:
        board[ord(c) - 65] += 1
    
    dp = [0 for _ in range(26)]
    for word in words:
        if all(map(lambda i: word[i] <= board[i], range(26))):
            for i in range(26):
                if word[i] > 0:
                    dp[i] += 1
    v_min = 200001
    v_max = 0
    for i in range(26):
        if board[i] > 0:
            v_min = min(v_min, dp[i])
            v_max = max(v_max, dp[i])
    answer = ""
    for i in range(26):
        if board[i] > 0 and dp[i] == v_min:
            answer += chr(i + 65)
    answer += " " + str(v_min) + " "
    for i in range(26):
        if board[i] > 0 and dp[i] == v_max:
            answer += chr(i + 65)
    answer += " " + str(v_max) + " "
    print(answer)