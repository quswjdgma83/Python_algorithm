def solution(new_id):
    answer = ''
    temp = []
    
    for i, c in enumerate(new_id):
        c = c.lower()#1
        c = ord(c)
        if (c >= 97 and c <= 122) or (c>=48 and c <=57) or c == 95 or c == 45 or c == 46 or c == 32:
            if len(temp) >= 1 and c == 46 and temp[-1] == 46:
                continue
            temp.append(c)#2, 3
    #----temp----
    for i, c in enumerate(temp):
        if (i == 0 or i == len(temp)-1) and c == 46:#4
            temp.pop(i)
            
    if temp == []:#5
        temp.append(97)
    #z-.
    if len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == 46:
            temp.pop(14)
    # print(temp)
    if len(temp) <= 2:
        while True:
            if len(temp) == 3:
                break
            a = temp[-1]
            temp.append(a)
    for t in temp:
        answer += chr(t)
    
    return answer