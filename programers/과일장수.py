def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    box = len(score) // m
    for i in range(box):
        answer += min(score[i*m:(i+1)*m])*m
    return answer