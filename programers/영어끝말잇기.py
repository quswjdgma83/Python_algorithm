from math import ceil

def solution(n, words):
    temp = []
    index = 0
    flag = False
    for idx, word in enumerate(words):
        if len(temp) == 0:
            temp.append(word)
            continue
        if word in temp or word[0] != temp[-1][-1]:
            index = idx
            flag = True
            break
        temp.append(word)
    if flag == False:
        return [0,0]
    else:
        a = index%n + 1
        b = ceil((index+1)/n)
        return [a,b]
    return answer