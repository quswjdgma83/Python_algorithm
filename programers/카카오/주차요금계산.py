from math import ceil

def sol(HHMM):
    a = HHMM.split(":")
    b = int(a[0])
    return b*60 + int(a[1])

def solution(fees, records):
    answer = []
    dict_a = {}
    #[시각, 기본요금, 단위시간, 단위요금]
    #[시간, 차량번호, 상태]
    for record in records:
        a = record.split(" ")
        if a[1] not in dict_a:
            dict_a[a[1]] = [sol(a[0])]
        else:
            dict_a[a[1]].append(sol(a[0]))
    for k in dict_a:
        if len(dict_a[k]) % 2 == 1:
            dict_a[k].append(1439)
    result = []
    # dict_a = sorted(dict_a.items(), key=lambda x: x[0])
    key = sorted(list(dict_a.keys()))
    dict_b = {}
    for k in key:
        dict_b[k] = dict_a[k]
    for k in dict_b:
        price = 0
        li = dict_b[k]
        for l in range(len(li)):
            if l % 2 == 0:
                price -= li[l]
            else:
                price += li[l]
        result.append(price)
    default = fees[0]
    for r in result:
        if r <= default:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+ ceil((r-default)/fees[2])*fees[3])
    
    return answer