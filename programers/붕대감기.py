# def make_attack_dict(attacks):
#     # 공격이 끝나는 시간
#     last_attack_time = attacks[len(attacks)-1][0]
#     # 공격 유 무 dict
#     attack_time_list = [ attacks[i][0] for i in range(len(attacks))]
#     attack_deal_list = [ attacks[i][1] for i in range(len(attacks))]
#     attack_time_dict = {}
#     k = 0
#     for i in range(last_attack_time+1):
#         if i not in attack_time_list:
#             attack_time_dict[i] = 0
#         else:
#             attack_time_dict[i] = attack_deal_list[k]
#             k += 1
#             print(k)
#     return attack_time_dict
def make_attack_dict(attacks):
    last_attack_time = attacks[-1][0]
    attack_time_dict = {i: 0 for i in range(last_attack_time + 1)}  # 모든 시간에 대해 0으로 초기화
    for attack_time, attack_deal in attacks:
        attack_time_dict[attack_time] = attack_deal  # 실제 공격 시간에 대한 피해량 업데이트

    return attack_time_dict


def solution(bandage, health, attacks):
    # bandage [시전시간, 초당회복량, 추가회복량]
    # health 최대 체력
    # attacks[공격시간, 피해량]
    # ([5, 1, 5], 30, [[2,10],[9,15],[10,5],[11,5])
    # ([3, 2, 7], 20,	[[1, 15], [5, 16], [8, 6]])
    answer = 0
    attack_time_dict = make_attack_dict(attacks)
    print(attack_time_dict)
    now_health = health
    heal_list = [ 0 for _ in range(len(attack_time_dict))]
    attack_list = []
    max_time = bandage[0]
    heal_ps = bandage[1]
    max_heal = bandage[2]
    #공격 리스트
    for i in range(len(attack_time_dict)):
        attack_list.append(attack_time_dict[i])
    #힐 리스트
    count = 0
    for i in range(len(attack_list)):
        if count == max_time-1 and attack_list[i] == 0:
            heal_list[i] = heal_ps + max_heal
            count = 0
        elif attack_list[i] == 0:
            heal_list[i] = heal_ps
            count += 1
        else:
            heal_list[i] = 0
            count = 0
    #사용자 체력
    for i in range(len(attack_list)):
        if now_health < 0:
            answer = -1
            continue
        if now_health < health:
            now_health += heal_list[i]
            if now_health >= health:
                now_health = health
        now_health -= attack_list[i]
    if now_health > 0:
        answer = now_health
    else:
        answer = -1
    # print(heal_list)
    # print(attack_list)
    # print(answer)
    return answer

# solution([5, 1, 5], 30, [[2,10],[9,15],[10,5],[11,5]])
a = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
print(a)