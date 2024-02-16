def solution(rank, attendance):
    answer = 0
    student_dic = {}
    index_dic = {}
    count = 0
    bump = []
    for idx in range(len(rank)):
        index_dic[rank[idx]] = count
        count += 1
    for i in range(len(rank)):
        student_dic[rank[i]] = attendance[i]
    for key, value in student_dic.items():
        if value == True:
            bump.append(key)
    bump = sorted(bump)
    a = bump[0]
    b = bump[1]
    c = bump[2]
    answer = index_dic[a]*10000 + index_dic[b]*100 + index_dic[c]
    return answer

solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])