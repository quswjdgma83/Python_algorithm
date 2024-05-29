def solution(score):
    answer = [0]*len(score)
    temp = []
    for sc in score:
        temp.append(sum(sc))
    cnt = 1
    while True:
        m = max(temp)
        cnt2 = -1
        if m == -1:
            break
        for i,t in enumerate(temp):
            if t == m:
                answer[i] = cnt
                temp[i] = -1
                cnt2 += 1
        cnt += (cnt2+1)
        
    return answer