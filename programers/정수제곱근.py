from math import sqrt

def solution(n):
    answer = 0
    a = sqrt(n)
    b = int(a)
    if a == b:
        answer = (b+1)**2
    else:
        answer = -1
    return answer