from collections import defaultdict

def solution(lines):
    answer = 0
    tar = []
    for line in lines:
        temp = []
        for l in range(line[0],line[1]):
            if l != line[1]:
                temp.append(l+0.5)
        tar.append(temp)
    # dict_a = {}
    dict_a = defaultdict(int)
    for ta in tar:
        for t in ta:
            # if t not in dict_a:
            #     dict_a[t] = 1
            # else:
            dict_a[t] += 1
    a = list(dict_a.values())
    for i in a:
        if i >= 2:
            answer += 1
    return answer