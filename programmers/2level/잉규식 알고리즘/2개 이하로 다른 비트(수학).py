def solution(numbers):
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer