from itertools import permutations, combinations
from functools import cmp_to_key

def solution(marbles):
    answer = []
    for count in range(1, len(marbles)+1):
        for permutation in permutations(marbles, count):
            left, right = 0, len(permutation) - 1
            leftSum, rightSum = 0, 0
            while left <= right:
                if left == right and leftSum == rightSum:
                    break
                if leftSum <= rightSum:
                    leftSum += permutation[left]
                    left += 1
                else:
                    rightSum += permutation[right]
                    right -= 1
            if leftSum == rightSum:
                answer.append([permutation, abs(len(permutation) - right - 1 - left)])

    def comp(x, y):
        if x[1] == y[1]:
            if len(x[0]) == len(y[0]):
                xSum, ySum = sum(x[0]), sum(y[0])
                if xSum == ySum:
                    for i in range(min(len(x[0]), len(y[0]))):
                        if x[0][i] == y[0][i]:
                            continue
                        return x[0][i] - y[0][i]
                return ySum - xSum
            return len(y[0]) - len(x[0])
        return x[1] - y[1]



    return sorted(answer, key=cmp_to_key(comp))[0][0]