from math import sqrt

def isSosu(num):
    flag = True
    if num == 1 or num == 0:
        return 0
    for n in range(2,int(sqrt(num))+1):
        if num % n == 0:
            flag = False
            break
    if flag == True:
        return 1
    else:
        return 0

def solution(n, k):
    answer = 0
    mok = -1
    na = 0
    temp = []
    while(mok != 0):
        mok = n // k
        na = n % k
        n = mok
        temp.append(str(na))
    temp.reverse()
    temp = "".join(temp)
    goal = temp.split("0")
    for go in goal:
        if go != '':
            answer += isSosu(int(go))

    return answer