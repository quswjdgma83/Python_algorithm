from collections import deque

def solution(s):
    target = [k for k in s]
    temp = deque()
    idx = 0
    while idx != len(target):
        if len(temp) == 0:
            temp.append(target[idx])
            idx += 1
            continue
        if temp[-1] == target[idx]:
            temp.pop()
        else:
            temp.append(target[idx])
        idx += 1
    if len(temp) != 0:
        return 0
    else:
        return 1
