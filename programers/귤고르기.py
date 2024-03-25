def solution(k, tangerine):
    answer = 0
    dict_a = {}
    for tang in tangerine:
        if tang not in dict_a:
            dict_a[tang] = 1
        else:
            dict_a[tang] += 1
    dict_b = sorted(dict_a, key = lambda x: dict_a[x])
    dict_b.reverse()
    a = 0
    idx = 0
    while(a < k):
        a += dict_a[dict_b[idx]]
        idx += 1
    answer  = idx
    return answer