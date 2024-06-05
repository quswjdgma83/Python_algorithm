from itertools import permutations

def solution(spell, dic):
    data = list(permutations(spell))
    temp = []
    for da in data:
        t = ""
        k = list(da)
        for i in k:
            t += i
        temp.append(t)
    for d in dic:
        if d in temp:
            return 1
    return 2