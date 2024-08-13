def solution(data, ext, val_ext, sort_by):
    # code, date, max, remain
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, 
    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    answer = []
    dict_a = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    target = dict_a[ext]
    
    for da in data:
        if da[target] < val_ext:
            answer.append(da)
    answer = sorted(answer, key = lambda x: x[dict_a[sort_by]])
    return answer