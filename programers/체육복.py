def solution(n, lost, reserve):
    _lost = [i-1 for i in lost if i not in reserve]
    _reserve = [i-1 for i in reserve if i not in lost]
    
    answer = n-len(_lost)
    
    target = [0 for _ in range(n)]
    for idx in _reserve:
        target[idx] = 1
    _lost = sorted(_lost)
    for l in _lost:
        if l != 0 and target[l-1] == 1:
            answer += 1
            target[l-1] = 0
        elif l != n-1 and target[l+1] == 1:
            answer += 1
            target[l+1] = 0
    return answer