def solution(id_list____, report, k):
    report = set(report)
    r_dict = {}
    k_dict = {}
    for goal in report:
        user, attacked = goal.split(" ")
        r_dict[user] = attacked
    report_list = list(r_dict.values())
    for id in id_list____:
        if report_list.count(id) >= k:
            k_dict[id] = True
        else:
            k_dict[id] = False
        
    result_dict = {}
    for user, attacked in r_dict.items():
        result_dict[user] = 0
        if k_dict[attacked] == True:#신고를 당했다면
            result_dict[user] += 1
    
    answer = list(result_dict.values())
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
