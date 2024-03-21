# from collections import deque

def solution(phone_book):
    answer = True
    pb = sorted(phone_book)
    # pb = deque(pb)
    for i in range(len(pb)):
        a = len(pb[i])
        for j in range(i+1, len(pb)):
            if pb[i] == pb[j][:a]:
                answer = False
                break
        if answer == False:
            break
    return answer

solution(["12","123","1235","567","88"])