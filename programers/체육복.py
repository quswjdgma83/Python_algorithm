def solution(n, lost, reserve):
    answer = 0
    lost = [k-1 for k in lost]
    lost = sorted(lost)
    reserve = [k-1 for k in reserve]
    reserve = sorted(reserve)
    now1 = [1 for _ in range(n)]
    now2 = [1 for _ in range(n)]
    for idx in range (n):
        if idx in lost:
            now1[idx] -= 1
        if idx in reserve:
            now1[idx] += 1
            
    for idx in range (n):
        #앞쪽에 빌림
        if idx > 0 and now1[idx] == 0:
            if now1[idx-1] == 2:
                now1[idx-1] = 1
                now1[idx] = 1
        #뒷쪽에 빌림
        elif idx < n-1 and now1[idx] == 0:
            if now1[idx+1] == 2:
                now1[idx+1] = 1
                now1[idx] = 1
    answer1 = n - now1.count(0)
    
    for idx in range (n):
        if idx in lost:
            now2[idx] -= 1
        if idx in reserve:
            now2[idx] += 1
            
    for idx in range (n):
        #뒷쪽에 빌림
        if idx < n-1 and now2[idx] == 0:
            if now2[idx+1] == 2:
                now2[idx+1] = 1
                now2[idx] = 1
        #앞쪽에 빌림
        elif idx > 0 and now2[idx] == 0:
            if now2[idx-1] == 2:
                now2[idx-1] = 1
                now2[idx] = 1
    answer2 = n - now2.count(0)
    answer = max(answer1, answer2)
    print(answer)
    return answer

solution(5, [5, 3], [4, 2])
