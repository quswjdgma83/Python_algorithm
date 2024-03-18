def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    [c1, c2, c3] = [0, 0, 0]
    for idx in range(len(answers)):
        if a1[idx % 5] == answers[idx]:
            c1 += 1
        if a2[idx % 8] == answers[idx]:
            c2 += 1
        if a3[idx % 10] == answers[idx]:
            c3 += 1
    if c1 == c2 == c3:
        return [1, 2, 3]
    temp = max(c1, c2, c3)
    ans = [c1,c2,c3]
    
    for idx, k in enumerate(ans):
        if k == temp:
            answer.append(idx+1)
    return answer