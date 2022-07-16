def solution(x):
    b = []
    for i in str(x):
        b.append(int(i))
    if int(x%sum(b)) == 0:
        return True
    else:
        return False