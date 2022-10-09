import itertools

def solution(nums):
    isPrime = [False, False] + [True for i in range(max(nums)*3)]
    for number in range(2, len(isPrime)):
        if isPrime[number]:
            for target in range(2*number, len(isPrime), number):
                isPrime[target] = False
    return len(list(filter(lambda x: isPrime[sum(x)], list(itertools.combinations(nums, 3)))))
