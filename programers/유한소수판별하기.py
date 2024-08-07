def sol(num):
    k = 1
    count = 0
    temp = []
    for i in range(1,num+1):
        if num % i == 0:
            temp.append(i)
    return temp

def sol2(num):
    count = 0
    for i in range(1,num//2 + 1):
        if num % i == 0:
            count += 1
    if count == 1:
        return "소인수"
    else:
        return "아님"

def sol3(num):
    k = 1
    count = 0
    temp = []
    for i in range(1,num+1):
        if num % i == 0 and sol2(i)=="소인수":
            temp.append(i)
    return temp

def solution(a, b):
    temp1 = sol(a)
    temp2 = sol(b)
    bump = []
    for i in temp1:
        if i in temp2:
            bump.append(i)
    k = max(bump)
    target = b//k
    
    goal = sol3(target)
    flag = True
    for g in goal:
        if g not in [1,2,5]:
            flag = False
    if flag:
        return 1
    else:
        return 2