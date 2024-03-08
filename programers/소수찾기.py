from math import sqrt

def count_num(num):
    count = 0
    for i in range(1, int(sqrt(num))+1):
        if count > 2:
            return 3
        if num % i == 0:
            count += 2
            if i**2 == num:
                count += 1
    return count

def solution(n):
    answer = 0
    temp = []
    for num in range(1, n+1):
        if count_num(num) == 2:
            temp.append(num)
    answer = len(temp)
    return answer