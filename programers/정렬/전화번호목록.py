def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    
    for ph in phone_book:
        for p in range(1,len(ph)):
            if ph[:p] in phone_book:
                return False
    return answer