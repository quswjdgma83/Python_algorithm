def sol(n):
    tar = n
    temp = []
    while(tar >= 1):
        temp.append(tar % 2)
        tar = tar // 2
    cnt = temp.count(1)
    return cnt

def solution(n):
    answer = 0
    a = n
    tar = sol(n)
    while True:
        a += 1
        if sol(a) == tar:
            return a
