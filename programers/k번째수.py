def solution(array, commands):
    answer = []
    for com in commands:
        st = com[0]
        end = com[1]
        idx = com[2]
        temp = sorted(array[st-1:end])
        answer.append(temp[idx-1])
    return answer
