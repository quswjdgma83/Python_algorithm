from itertools import permutations
from math import sqrt

def isSosu(num):
    flag = True
    if num == 1 or num == 0:
        return 0
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        return 1
    else:
        return 0

def solution(numbers):
    answer = 0
    numbers = [i for i in numbers]
    temp = []
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers,i):
            temp.append(int("".join(num)))
    temp = sorted(list(set(temp)))
    print(temp)
    for te in temp:
        answer += isSosu(te)
    return answer