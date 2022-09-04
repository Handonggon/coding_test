def solution(str1, str2):
    str1,str2 = str1.upper(),str2.upper()
    dic = [chr(i) for i in range(65,91)]
    A = [str1[i]+str1[i+1] for i in range(len(str1)-1) if str1[i] in dic and str1[i+1] in dic]
    B = [str2[i]+str2[i+1] for i in range(len(str2)-1) if str2[i] in dic and str2[i+1] in dic]
    
    temp_A = A[:]
    temp_B = B[:]
    interection = []
    union = A[:]
    for i in B :
        if i not in temp_A :
            union.append(i)
        else :
            temp_A.remove(i)
    for i in A :
        if i in temp_B :
            interection.append(i)
            temp_B.remove(i)
    
    if len(union) == 0 :
        return 65536
    else :
        return int("{0:.0f}".format(len(interection)/len(union) * 65536-0.5))
