def solution(x, n):
    answer = []
    k = x
    for _ in range(n):
        answer.append(x)
        x += k
    return answer