def solution(number):
    answer = 0
    num = number
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if num[i] + num[j] + num[k] == 0:
                    answer += 1
    return answer