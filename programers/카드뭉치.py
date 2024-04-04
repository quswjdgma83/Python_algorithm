def solution(cards1, cards2, goal):
    answer = ''
    temp1 = []
    temp2 = []
    t1 = {}
    t2 = {}
    for i, card in enumerate(cards1):
        t1[card] = i
        
    for i, card in enumerate(cards2):
        t2[card] = i
        
    flag = True
    for go in goal:
        flag_f = flag
        if go in cards1:
            temp1.append(t1[go])
            flag = not flag
        else:
            temp2.append(t2[go])
            flag = not flag
        if flag_f == flag:
            return "No"
    for i in range(1,len(temp1)):
        if temp1[i] != i:
            return "No"
    for i in range(1,len(temp2)):
        if temp2[i] != i:
            return "No"
    return "Yes"