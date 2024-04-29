def solution(n, left, right):
    answer = []
    for index in range(left, right + 1):
        i = index // n
        j = index % n
        answer.append(max(i, j) + 1)
    return answer
