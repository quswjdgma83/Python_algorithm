def sol1(x):
    k = ""
    t = 0
    for i in x:
        if i == "1":
            k += i
        else:
            t += 1
    return k, t

def sol2(x):
    a = len(x)
    b = ""
    while a >= 1:
        b += str(a % 2)
        a = a//2
    c = ""
    for i in range(len(b)-1,-1,-1):
        c += b[i]
    return c

def solution(s):
    cnt = 0
    zcnt = 0
    a = s
    while a != "1":
        a, t = sol1(a)
        b = sol2(a)
        a = b
        cnt += 1
        zcnt += t
    return [cnt, zcnt]