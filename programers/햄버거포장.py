def solution(ingredient):
    # 3:고기 2:야채 1:빵
    # 패턴: [1,2,3,1]
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1
    return answer
