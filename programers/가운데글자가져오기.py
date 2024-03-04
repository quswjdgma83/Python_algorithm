def solution(s):
    cen = len(s)//2
    if len(s) % 2 == 0:
        return s[cen-1:cen+1]
    return s[cen]