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
    for i in range(1,(num+1)//2):
        if num % i == 0:
            count += 1
    if count == 1:
        return "소인수"
    else:
        return "아님"
        

def solution(a, b):
    temp1 = sol(a)
    temp2 = sol(b)
    # print(sol(a))
    # print(sol(b))
    bump = []
    for i in temp1:
        if i in temp2:
            bump.append(i)
    # print(max(bump))
    k = max(bump)
    target = b//k
    
    goal = sol(target)
    print(goal)
    flag = True
    for g in goal:
        if g not in [1,2,5]:
            flag = False
    if flag:
        return 1
    else:
        return 2