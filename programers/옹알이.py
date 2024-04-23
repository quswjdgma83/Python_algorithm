from itertools import permutations

def solution(babbling):
    ps = ["aya", "ye", "woo", "ma"]
    t4 = list(permutations(ps))
    t3 = list(permutations(ps,3))
    t2 = list(permutations(ps,2))
    temp = []
    answer = 0
    
    for s in t4:
        temp.append("".join(s))
    for s in t3:
        temp.append("".join(s))
    for s in t2:
        temp.append("".join(s))
    for s in ps:
        temp.append("".join(s))
    for b in babbling:
        if b in temp:
            answer += 1
    return answer