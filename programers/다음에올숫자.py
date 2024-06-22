def solution(common):
    #등차수열
    if (common[2] - common[1]) == (common[1] - common[0]):
        a = common[2] - common[1]
        return common[-1] + a
    else:
        b = common[2] // common[1]
        return common[-1] * b
