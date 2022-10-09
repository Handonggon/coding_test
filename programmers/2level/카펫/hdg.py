def solution(brown, yellow):
    total = brown + yellow
    count = 3
    while count != 2:
        if total % count == 0:
            if yellow == (count-2)*(int(total/count)-2):
                return [int(total/count),count]
            else:
                pass
        else:
            pass
        count += 1