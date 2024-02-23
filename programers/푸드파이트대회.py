def solution(food):
    answer = ''
    bump = []
    foodDict = {}
    #{1: 1, 2: 2, 3:3}
    for idx, kar in enumerate(food):
        if idx != 0:
            foodDict[idx] = kar//2
    for key, idx in foodDict.items():
        for _ in range(idx):
            bump.append(str(key))
    bump2 = list(reversed(bump))
    bump.append("0")
    bump = "".join(bump)
    print(bump)
    bump2 = "".join(bump2)
    answer = bump + bump2
    print(answer)
    return answer

solution([1, 3, 4, 6])
# 결과: "1223330333221"