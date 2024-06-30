def solution(arr, queries):
    answer = []
    for que in queries:
        [s, e, k] = que
        temp = []
        for i, a in enumerate(arr):
            if i >= s and i <= e:
                if arr[i] > k:
                    temp.append(arr[i])
        # print(temp)
        if len(temp) == 0:
            answer.append(-1)
            continue
        answer.append(min(temp))
    return answer