def solution(n, words):
    word = [words[0][0]]
    for c in range(len(words)//n):
        b = 0
        while b != n:
            if words[b+n*c][0] != word[-1][-1]:
                return [b+1, c+1]
            elif words[b+n*c] in word:
                return [b+1, c+1]
            word.append(words[b+n*c])
            b+=1
    return [0,0]