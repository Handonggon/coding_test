def solution(word): 
    word_list = ['A','E','I','O','U']
    temp_list = []
    
    for i in range(4) :
        for a in word_list :
            for b in ['A','E','I','O','U'] :
                temp_list.append(a+b)
        word_list += temp_list
    
    word_list = list(set(word_list))
    word_list = sorted(word_list)
    
    return word_list.index(word)+1