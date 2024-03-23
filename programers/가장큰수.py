from itertools import product

def solution(numbers):
    answer = ''
    numbers = list(product(numbers, repeat=len(numbers)))
    temp = []
    flag = False
    for num in numbers:
        if len(set(num)) == 3:
            temp.append(num)
    bp = ""
    bump = []
    for te in temp:
        for t in te:
            bp += str(t)
        bump.append(bp)
        bp = ""
    bump.sort(reverse=True)
    print(bump)
    answer = bump[0]
    return answer

solution([6, 10, 2])