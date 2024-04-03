def solution(dartResult):
    answer = 0
    nums = ["0","1","2","3","4","5","6","7","8","9","10"]
    bonus = {"S":1,"D":2,"T":3}
    temp = []
    flag = False
    for idx, t in enumerate(dartResult):
        if t in nums:
            if flag == True:
                flag = False
                continue
            if idx != len(dartResult)-1 and dartResult[idx+1] == "0":
                temp.append(10)
                flag = True
                continue
            temp.append(int(t))
        elif t in bonus:
            a = temp.pop()
            temp.append(a**bonus[t])
        else:
            if t == "*":
                if len(temp) == 1:
                    a = temp.pop()
                    temp.append(a*2)
                else:
                    b = temp.pop()
                    a = temp.pop()
                    temp.append(2*a)
                    temp.append(2*b)
            else:
                a = temp.pop()
                temp.append(-1*a)
    for n in temp:
        answer += n
    return answer