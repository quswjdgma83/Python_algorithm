def solution(name, yearning, photo):
    answer = []
    dict_score = {}
    score = [0]*len(name)
    for y in range(len(yearning)):
        score[y] = yearning[y]
    for n in range(len(name)):
        if name[n] not in dict_score:
            dict_score[name[n]] = score[n]
    print(dict_score)
    for i in range(len(photo)):
        s = 0
        for j in range(len(photo[i])):
            name = photo[i][j]
            if name in dict_score.keys():
                s += dict_score[name]
            else:
                continue
        answer.append(s)
    return answer