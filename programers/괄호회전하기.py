from collections import deque

left = ["[","{","("]
right = ["]","}",")"]

dict_a = {"[":"]", "{": "}","(":")"}

def search(s):
    stack = []
    flag = True
    for i, gal in enumerate(s):
        if gal in left:
            stack.append(gal)
        else:
            if len(stack) == 0:
                flag = False
                break
            a = stack.pop()
            b = left.index(a)
            
            if dict_a[a] != gal:
                flag = False
                break
    if len(stack) != 0:
        return 0
    if flag == True:
        return 1
    else:
        return 0

def solution(s):
    count = 0
    s = deque(s)
    for i in range(len(s)):
        if i != 0:
            s.rotate()
        count += search(s)
    answer = count
    print(answer)
    return answer