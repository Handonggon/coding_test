def solution(w,h):
    max = 0
    for i in range(1,min(w,h)+1) :
        if w%i==0 and h%i == 0 :
            max = i
    
    return w*h - (w+h-max)