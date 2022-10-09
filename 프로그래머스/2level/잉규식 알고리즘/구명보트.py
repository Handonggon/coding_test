def solution(people, limit) :
    people.sort(reverse=True)
    i = 0
    while i <= len(people) -1 :
        if people[i] + people[-1] <= limit :
            people.pop()
        i += 1
    return i