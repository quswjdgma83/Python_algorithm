from collections import deque

def sol(outq, inq):
    a = outq.popleft()
    inq.append(a)
    return a, outq, inq

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    maxx = len(queue1)*3
    sq1r = sum(queue1)
    sq2r = sum(queue2)
    while sq1r != sq2r:
        if sq1r > sq2r:
            val, queue1, queue2 = sol(queue1, queue2)
            sq1r -= val
            sq2r += val
        else:
            val, queue2, queue1 = sol(queue2, queue1)
            sq2r -= val
            sq1r += val
        cnt += 1
        if cnt > maxx:
            return -1
    answer = cnt
    return answer