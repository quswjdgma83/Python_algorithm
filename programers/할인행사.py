def solution(want, number, discount):
    answer = 0
    count = 0
    ww = 0
    for num in number:
        count += num
    for i in range(len(discount)-count+1):
        flag = False
        a = discount[i:i+count]
        temp = [] 
        ww += 1
        for w in range(len(want)):
            temp.append(a.count(want[w]))
            # print(temp)
            if temp[w] < number[w]:
                flag = True
                # print(True)
                break
        if flag == True:
            continue
        answer += 1
    # print(ww)
    return answer