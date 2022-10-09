def solution(phone_book):
    answer = True
    dic_book = {}
    for i in phone_book :
        if len(i) not in dic_book.keys() :
            dic_book[len(i)] = []
            dic_book[len(i)].append(i)
        else :
            dic_book[len(i)].append(i)
    dic_book = dict(sorted(dic_book.items()))
    for i in phone_book :
        s = len(i)
        for key,value in dic_book.items() :
            if s != key and i[:key] in value:
                return False
    return answer
