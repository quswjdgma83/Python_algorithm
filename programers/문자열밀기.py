from collections import deque

def solution(A, B):
    answer = 0
    A = deque([i for i in A])
    B = deque(B)
    if A == B:
        return 0
    for i in range(len(A)-1):
        temp = A.pop()
        A.appendleft(temp)
        if A == B:
            return i + 1
    return -1