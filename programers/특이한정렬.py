def solution(numlist, n):
    sorted_numlist = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return sorted_numlist