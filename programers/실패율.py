def solution(N, stages):
    lv_dict = {}
    for stage in stages:
        if stage <= N:
            if stage not in lv_dict:
                lv_dict[stage] = 1
            else:
                lv_dict[stage] += 1
    
    total_users = len(stages)
    fail_rates = []
    
    for stage in range(1, N+1):
        if stage in lv_dict:
            fail_rate = lv_dict[stage] / total_users
            total_users -= lv_dict[stage]
        else:
            fail_rate = 0
        fail_rates.append((stage, fail_rate))
    
    fail_rates.sort(key=lambda x: x[1], reverse=True)
    answer = [stage[0] for stage in fail_rates]
    
    return answer

# 예시 실행
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
