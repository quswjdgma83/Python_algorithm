def solution(priorities, location):
    #먼저 출력되는 index 쌓은 리스트
    answer = []
    prior = max(priorities)
    idx = priorities.index(prior)
    idx_f = idx
    while(prior != 0):
        if prior in priorities:
            idx = idx_f
            for _ in range(len(priorities)):
                if(prior == priorities[idx]):
                    answer.append(idx)
                    idx_f = idx
                idx = (idx+1)%(len(priorities))
        prior -= 1
    print(answer)
    num = answer.index(location)
    print(num+1)
    return num+1

# solution([2, 1, 3, 2], 2)
solution([2,3,3,2,9,3,3], 3)
# solution([5, 4, 3, 2, 1], 0)