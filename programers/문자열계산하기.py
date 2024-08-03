def solution(my_string):
    answer = 0
    temp = my_string.split(" ")
    temp1 = []
    temp2 = []
    for t in temp:
        if t == "+" or t == "-":
            if t == "+":
                temp1.append(1)
            else:
                temp1.append(-1)
        else:
            temp2.append(int(t))
    for i, t in enumerate(temp2):
        if i == 0:
            answer += t
        else:
            answer += t*temp1[i-1]
    return answer