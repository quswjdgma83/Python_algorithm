def solution(friends, gifts):
    answer = []
    #경우의수: 1. 선물을 주고받은 기록 2. 선물지수: 준선물수 - 받은선물수
    #gifts[0] 선물을 준 친구
    #gifts[1] 선물을 받은 친구
    dict_a = {}
    dict_b = {}
    for f in friends:
        dict_a[f] = 0
        dict_b[f] = []
    for gi in gifts:
        fr, to = gi.split(" ")
        dict_a[fr] += 1
        dict_a[to] -= 1
        dict_b[fr].append(to) 

    for gi in gifts:
        fr, to = gi.split(" ")
        if fr in dict_b[to]:
            dict_b[to].pop(dict_b[to].index(fr))
            
    for di in dict_b:
        dict_b[di] = list(set(dict_b[di]))
    # print(dict_a)
    # print(dict_b)
    for di in dict_b:
        temp = []
        cnt = 0
        cnt += len(dict_b[di])
        temp = [f for f in friends if f not in dict_b[di] and f != di and di not in dict_b[f]]
        for t in temp:
            if dict_a[di] > dict_a[t] and di not in dict_b[t]:
                cnt += 1
        answer.append(cnt)
    #     print(temp)
    # print(answer)
    return max(answer)