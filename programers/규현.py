def solution(n, scores):
    answer = []
    count = 0
    rank = 1
    scores = sorted(scores, reverse=True)
    x = []
    y = []
    flag = False
    for idx in range(len(scores)):
        if idx == len(scores)-1:
            next_a = 0
            next_b = 0
        else:
            next_a = scores[idx+1][0]
            next_b = scores[idx+1][1]

        a = scores[idx][0]
        b = scores[idx][1]
        #리스트 요소내의 아무 수와 비교해도 작다면 flag = True
        if len(x) != 0:
            temp = 0
            for i in range(len(x)):
                if (a < min(x) and b < min(y)):
                    flag = False
                    break
                else:
                    flag = True

        #rank 통과x
        if (a < next_a or b < next_b or (a == next_a and b == next_b)) and flag == True:
            count += 1
        #rank 통과조건
        elif((next_a < a and next_b < b) or (next_a == a and next_b < b) or (next_a < a and next_b == b)) or flag == False:
            x = []
            y = []
            for _ in range(count):
                answer.append(rank)
            rank += count
            count = 1


        x.append(a)
        y.append(b)

        flag = False


    print(answer)
    return answer

# solution(2,[[62,53], [36, 53]])
solution(5,[[68,73], [71, 56], [56, 64], [18, 22], [15, 23]])
# solution(6,[[68,73], [71, 56], [56, 64], [], [18, 22], [15, 23]])
