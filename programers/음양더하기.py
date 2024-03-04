def solution(absolutes, signs):
    answer = 0
    for s in range(len(signs)):
        if signs[s] == False:
            absolutes[s] = absolutes[s] * (-1)
        answer += absolutes[s]
    
    return answer