from itertools import combinations
from math import sqrt

def isSosu(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    a = combinations(nums,3)
    target = []
    for i in a:
        target.append(sum(i))
    for t in target:
        if isSosu(t):
            answer += 1
    return answer