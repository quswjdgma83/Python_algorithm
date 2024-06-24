def minus(sc):
    if sc == 4:
        return 0
    else:
        return 8 - sc
def plus(sc):
    if sc == 4:
        return 0
    else:
        return sc
    

def solution(survey, choices):
    answer = ''
    #R T
    #C F
    #J M
    #A N
    #survey 비동의 동의
    #choices 1 -> 7 [1,2,3,4,5,6,7]
    mbti = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }
    for i, surv in enumerate(survey):
        f, s = surv[0], surv[1]
        mbti[f] += minus(choices[i])
        mbti[s] += plus(choices[i])
    print(mbti)
    temp = list(mbti.keys())
    temp2 = list(mbti.values())
    print(temp)
    for i, t in enumerate(temp):
        if i % 2 == 1:
            continue
        k = i % 2
        if temp2[i] > temp2[i+1]:
            answer += temp[i]
        elif temp2[i] == temp2[i+1]:
            answer += temp[i]
        else:
            answer += temp[i+1]
    return answer