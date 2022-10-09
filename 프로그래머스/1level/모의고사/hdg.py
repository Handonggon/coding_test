def solution(answers):
    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    score = [0 for i in range(len(students))]
    for index in range(len(answers)):
        for number in range(len(students)):
            score[number] += 1 if students[number][index%len(students[number])]==answers[index] else 0
    return list(map(lambda x: x+1, filter(lambda x: score[x] == max(score), range(len(score)))))
