def solution(num):
    answer = 0
    bump = num
    while bump != 1:
        if bump % 2 == 0:
            bump = bump//2
        elif bump % 2 == 1:
            bump = bump*3 + 1
        if answer >= 500:
            return -1
        answer += 1
    return answer