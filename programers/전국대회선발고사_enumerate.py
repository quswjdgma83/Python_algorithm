def solution(rank, attendance):
    answer = 0
    bump = []
    for idx, value in enumerate(attendance):
        if value:
            bump.append(rank[idx])
    bump.sort()
    answer = 10000*rank.index(bump[0]) + 100*rank.index(bump[1]) + rank.index(bump[2])
    print(answer)
    return answer

solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])