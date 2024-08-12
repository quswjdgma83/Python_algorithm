def solution(d, budget):
    answer = 0
    de = sorted(d, reverse = True)
    temp = budget
    while True:
        if len(de) > 0 and de[-1] <= temp:
            t = de.pop()
            # print(de, temp)
            temp -= t
            answer += 1
        else:
            break
    return answer