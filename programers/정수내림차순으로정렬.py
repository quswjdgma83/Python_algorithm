def solution(n):
    answer = ""
    n = str(n)
    dict_a = {}
    for i in n:
        if i not in dict_a:
            dict_a[i] = 1
        else:
            dict_a[i] += 1
    dict_b = {key: dict_a[key] for key in sorted(dict_a)}
    temp = ""
    for k,v in dict_b.items():
        for _ in range(v):
            temp += k
    temp1 = [i for i in temp]
    temp2 = reversed(temp1)
    for i in temp2:
        answer += i
    answer = int(answer)
    return answer