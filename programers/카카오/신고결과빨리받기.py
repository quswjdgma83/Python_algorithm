def solution(id_list, report, k):
    answer = []
    dict_a = {}
    dict_b = {}
    for id in id_list:
        dict_a[id] = []
        dict_b[id] = 0
    
    for re in report:
        f, t = re.split(" ")
        if t not in dict_a[f]:
            dict_a[f].append(t)
    
    prison_y = list(dict_a.values())
    for pri in prison_y:
        for p in pri:
            dict_b[p] += 1
    prison = []
    for tar in dict_b:
        if dict_b[tar] >= k:
            prison.append(tar)
    # print(dict_a)
    # print(dict_b)
    # print(prison)
    for di in dict_a:
        cnt = 0
        temp = dict_a[di]
        for te in temp:
            if te in prison:
                cnt += 1
        answer.append(cnt)
            
    return answer