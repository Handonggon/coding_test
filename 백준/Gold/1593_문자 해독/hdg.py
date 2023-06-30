import sys
input = sys.stdin.readline

def getWord(s):
    word = {}
    for c in s:
        word[c] = (word[c] + 1 if c in word else 1)
    return word

[w, g] = map(int, input().split())
W = input().strip()
S = input().strip()

word = [0 for _ in range(58)]
window = [0 for _ in range(58)]
for i in range(w):
    word[ord(W[i]) - 65] += 1

answer = 0
for right in range(g):
    left = right + 1 - w
    window[ord(S[right]) - 65] += 1
    if word == window:
        answer += 1
    if left >= 0: window[ord(S[left]) - 65] -= 1
print(answer)