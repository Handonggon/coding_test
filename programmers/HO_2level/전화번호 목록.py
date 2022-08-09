def solution(phone_book):
    
    phone_book = list(map(int, phone_book))
    phone_book.sort()
    
    while True:
        if phone_book:
            a = phone_book.pop(0)
            for i in phone_book:
                if str(a) in str(i):
                    return False
        else:
            break
            
    return True