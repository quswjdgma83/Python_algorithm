from math import sqrt
#number: 기사단원의 수
#limit: 협약 공격력 max
#power: 협약 초과 무기 공격력


def yaksu(number):
    count = 0
    for i in range(1, int(sqrt(number) + 1)):
        if number % i == 0:
            count += 1
            if number != i**2:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        bump = yaksu(num)
        if bump > limit:
            answer += power
        else:
            answer += bump
    return answer